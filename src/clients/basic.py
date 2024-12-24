"""Module basic.py"""
import logging

import gradio
import transformers

import config


class Basic:
    """
    Notes<br>
    -----<br>

    This class launches an illustrative graphical user interface for interacting
    with the token classification model.  It can be as simple or advanced as required
    because the underlying software allows for extensive customisation.
    """

    def __init__(self, path: str):
        """

        :param path: The model's path
        """

        self.__configurations = config.Config()

        # Pipeline
        self.__classifier = transformers.pipeline(task='ner', model=path, device=self.__configurations.device)

    def __basic(self, paragraph):
        """

        :param paragraph:
        :return:
        """

        tokens = self.__classifier(paragraph)

        return {'text': paragraph, 'entities': tokens}

    def exc(self):
        """

        :return:
        """

        demo = gradio.Interface(self.__basic,
                                gradio.Textbox(placeholder="Enter sentence here..."),
                                gradio.HighlightedText(),
                                examples=self.__configurations.examples)
        logging.info('Launching basic interface ...')
        demo.launch()
