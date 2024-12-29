"""Module future.py"""
import logging
import os
import subprocess

import gradio
import pandas as pd
import transformers

import config
import src.algorithms.interface
import src.elements.s3_parameters as s3p
import src.elements.service as sr
import src.functions.cache
import src.transfer.interface


class Future:
    """
    A set-up that allows for custom interface options.
    """

    def __init__(self, service: sr.Service, s3_parameters: s3p.S3Parameters):
        """

        :param service: A suite of services for interacting with Amazon Web Services.
        :param s3_parameters: The overarching S3 (Simple Storage Service) parameters
                              settings of this project, e.g., region code name, buckets, etc.
        """

        self.__service: sr.Service = service
        self.__s3_parameters: s3p.S3Parameters = s3_parameters

        # Instances
        self.__configurations = config.Config()
        self.__algorithms = src.algorithms.interface.Interface()

        # Pipeline
        self.__classifier = transformers.pipeline(
            task='ner', model=os.path.join(self.__configurations.data_, 'model'),
            config=os.path.join(self.__configurations.data_, 'model'),
            tokenizer=os.path.join(self.__configurations.data_, 'model'),
            device=self.__configurations.device)

    def __custom(self, text):
        """

        :param text:
        :return:
        """

        tokens = self.__classifier(text)
        summary = pd.DataFrame.from_records(data=tokens)
        summary = summary.copy()[['word', 'entity', 'score']]

        # For the future
        self.__algorithms.exc(text=text, tokens=tokens)

        return {'text': text, 'entities': tokens}, summary.to_dict(orient='records'), tokens

    def __kill(self) -> str:
        """

        :return:
        """

        logging.info('Transferring & Terminating')

        # Transferring interactions data, and delete cache points
        src.transfer.interface.Interface(service=self.__service, s3_parameters=self.__s3_parameters).exc()
        src.functions.cache.Cache().exc()

        return subprocess.check_output('kill -9 $(lsof -t -i:7860)', shell=True, text=True)

    def exc(self):
        """
        Upcoming: If Stop|Private, do not transfer inputs to Amazon S3 (Simple Storage Service)

        :return:
        """

        with gradio.Blocks() as demo:

            gradio.Markdown(value=('<h1>Token Classification</h1><br><b>An illustrative interactive interface; the interface '
                                   'software allows for advanced interfaces.</b>'), line_breaks=True)

            with gradio.Row():
                with gradio.Column(scale=3):
                    text = gradio.Textbox(label='TEXT', placeholder="Enter sentence here...", max_length=2000)
                with gradio.Column(scale=2):
                    detections = gradio.HighlightedText(label='DETECTIONS', interactive=False)
                    scores = gradio.JSON(label='SCORES')
                    compact = gradio.Textbox(label='COMPACT')
            with gradio.Row():
                detect = gradio.Button(value='Submit')
                gradio.ClearButton([text, detections, scores, compact])
                stop = gradio.Button('Stop', variant='stop', visible=True, size='lg')

            detect.click(self.__custom, inputs=text, outputs=[detections, scores, compact])
            stop.click(fn=self.__kill)
            gradio.Examples(examples=self.__configurations.examples, inputs=[text], examples_per_page=1)

        demo.launch(server_port=7860)
