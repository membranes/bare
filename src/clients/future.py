"""Module future.py"""
import logging
import subprocess

import gradio
import transformers

import config
import src.clients.persist


class Future:
    """
    A set-up that allows for custom interface options.
    """

    def __init__(self, path: str):
        """

        :param path: The path to the underlying model's artefacts
        """

        self.__configurations = config.Config()
        self.__persist = src.clients.persist.Persist()

        # Pipeline
        self.__classifier = transformers.pipeline(task='ner', model=path, device=self.__configurations.device)

    def __custom(self, paragraph):
        """

        :param paragraph:
        :return:
        """

        tokens = self.__classifier(paragraph)
        summary = {token['word']: [token['entity'], token['score']] for token in tokens}

        self.__persist.exc(paragraph=paragraph, summary=summary, tokens=tokens)

        return {'text': paragraph, 'entities': tokens}, summary, tokens

    @staticmethod
    def __kill() -> str:
        """

        :return:
        """

        logging.info('Terminating ...')

        return subprocess.check_output('kill -9 $(lsof -t -i:7860)', shell=True, text=True)

    def exc(self):
        """

        :return:
        """

        with gradio.Blocks() as demo:

            gradio.Markdown(value=('<h1>Token Classification</h1><br><b>An illustrative interactive interface; the interface '
                                   'software allows for advanced interfaces.</b>'), line_breaks=True)

            with gradio.Row():
                with gradio.Column(scale=3):
                    with gradio.Row():
                        paragraph = gradio.Textbox(label='paragraph', placeholder="Enter sentence here...", max_length=2000)
                with gradio.Column(scale=2):
                    with gradio.Row():
                        with gradio.Column():
                            detections = gradio.HighlightedText(label='detections', interactive=True)
                            scores = gradio.JSON(label='scores')
                            compact = gradio.Textbox(label='compact')
            with gradio.Row():
                with gradio.Row():
                    detect = gradio.Button(value='Submit')
                    gradio.ClearButton([paragraph, detections, scores, compact])
                    stop = gradio.Button('Stop', variant='stop', visible=True, size='lg')

            detect.click(self.__custom, inputs=paragraph, outputs=[detections, scores, compact])
            stop.click(fn=self.__kill)
            gradio.Examples(examples=self.__configurations.examples, inputs=[paragraph], examples_per_page=1)

        demo.launch(server_port=7860)
