"""Module basic.py"""
import logging
import os

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

    def __init__(self):
        """
        Constructor
        """

        self.__configurations = config.Config()

        # Pipeline
        self.__classifier = transformers.pipeline(
            task='ner', model=os.path.join(self.__configurations.data_, 'model'),
            device=self.__configurations.device)

        self.__css = (
            '.gradio-container-5-9-1 .prose table, .gradio-container-5-9-1 .prose tr, '
            '.gradio-container-5-9-1 .prose td, .gradio-container-5-9-1 .prose th '
            '{border:0 solid var(--body-text-color);}'
            '.paginate.svelte-p5q82i.svelte-p5q82i.svelte-p5q82i '
            '{justify-content:left; font-size:var(--text-md); margin-left: 10px;}')

    @staticmethod
    def __table(tokens) -> str:
        """

        :param tokens:
        :return:
        """

        head = (
            '<table style="width: 35%; font-size: 90%; text-align: left;">'
            '<colgroup>'
            '<col span="1" style="width: 10%;"><col span="1" style="width: 10%;"><col span="1" style="width: 10%;">'
            '</colgroup>'
            '<thead style="background: orange; font-weight: bold;">'
            '<tr><th>word</th><th>entity</th><th>score</th></tr>'
            '</thead>')

        for token in tokens:
            head = head + f"<tr><td>{token['word']}</td><td>{token['entity']}</td><td>{token['score']:.3f}</td></tr>"

        head = head + '</table>'

        return head

    def __basic(self, paragraph):
        """

        :param paragraph:
        :return:
        """

        tokens = self.__classifier(paragraph)
        table = self.__table(tokens=tokens)

        return {'text': paragraph, 'entities': tokens}, table

    def exc(self):
        """

        :return:
        """

        demo = gradio.Interface(self.__basic,
                                gradio.Textbox(placeholder="Enter sentence here..."),
                                [gradio.HighlightedText(), 'html'],
                                examples=self.__configurations.examples, css=self.__css)

        logging.info('Launching basic interface ...')

        demo.launch()
