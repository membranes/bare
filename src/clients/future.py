"""Module future.py"""
import logging
import os
import subprocess
import pandas as pd

import gradio
import transformers

import config
import src.algorithms.interface


class Future:
    """
    A set-up that allows for custom interface options.
    """

    def __init__(self):
        """

        Constructor
        """

        self.__configurations = config.Config()
        self.__algorithms = src.algorithms.interface.Interface()

        # Pipeline
        self.__classifier = transformers.pipeline(
            task='ner', model=os.path.join(self.__configurations.data_, 'model'),
            config=os.path.join(self.__configurations.data_, 'model'),
            tokenizer=os.path.join(self.__configurations.data_, 'model'),
            device=self.__configurations.device)

    def __custom(self, paragraphs):
        """

        :param paragraphs:
        :return:
        """

        tokens = self.__classifier(paragraphs)
        summary = pd.DataFrame.from_records(data=tokens)
        summary = summary.copy()[['word', 'entity', 'score']]

        # For the future
        self.__algorithms.exc(paragraphs=paragraphs, tokens=tokens)

        return {'text': paragraphs, 'entities': tokens}, summary.to_dict(orient='records'), tokens

    @staticmethod
    def __kill() -> str:
        """

        :return:
        """

        logging.info('Terminating ...')

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
                    paragraphs = gradio.Textbox(label='paragraphs', placeholder="Enter sentence here...", max_length=2000)
                with gradio.Column(scale=2):
                    detections = gradio.HighlightedText(label='detections', interactive=False)
                    scores = gradio.JSON(label='scores')
                    compact = gradio.Textbox(label='compact')
            with gradio.Row():
                detect = gradio.Button(value='Submit')
                gradio.ClearButton([paragraphs, detections, scores, compact])
                stop = gradio.Button('Stop', variant='stop', visible=True, size='lg')

            detect.click(self.__custom, inputs=paragraphs, outputs=[detections, scores, compact])
            stop.click(fn=self.__kill)
            gradio.Examples(examples=self.__configurations.examples, inputs=[paragraphs], examples_per_page=1)

        demo.launch(server_port=7860)
