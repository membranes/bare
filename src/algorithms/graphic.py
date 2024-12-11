"""Module graphic.py"""
import logging
import transformers
import gradio


class Graphic:
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

        self.__examples = [
            ['The English writer and the Afghani soldier.'],
            ['It was written by members of the United Nation.'],
            [('There were more than a hundred wolves in the Tiger Basin.  It is a dangerous place '
            'after 9 p.m., especially near Lake Victoria.')]]

        # Pipeline
        self.__classifier = transformers.pipeline(task='ner', model=path, device='cuda')
        logging.info(self.__classifier)

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
            '<thead style="background: orange; font-weight: bold;"><tr><th>word</th><th>entity</th><th>score</th></tr></thead>')

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

        return {'text': paragraph, 'entities': tokens}

    def __custom(self, paragraph):
        """

        :param paragraph:
        :return:
        """

        tokens = self.__classifier(paragraph)

        table = self.__table(tokens=tokens)
        logging.info(table)

        summary = {token['word']: [token['entity'], token['score']] for token in tokens}
        logging.info(summary)

        return {'text': paragraph, 'entities': tokens}, summary, table

    def exc(self, basic: bool = True):
        """

        :param basic: Basic interface?
        :return:
        """

        css = ('.gradio-container-5-8-0 .prose table, .gradio-container-5-8-0 .prose tr, '
               '.gradio-container-5-8-0 .prose td, .gradio-container-5-8-0 .prose th '
               '{border:0 solid var(--body-text-color);}'
               '.paginate.svelte-p5q82i.svelte-p5q82i.svelte-p5q82i '
               '{justify-content:left; font-size:var(--text-md); margin-left: 10px;}')

        if basic:
            demo = gradio.Interface(self.__basic,
                                    gradio.Textbox(placeholder="Enter sentence here..."),
                                    gradio.HighlightedText(),
                                    examples=self.__examples)
        else:
            demo = gradio.Interface(self.__custom,
                                    gradio.Textbox(placeholder="Enter sentence here..."),
                                    [gradio.HighlightedText(), 'json', 'html'],
                                    examples=self.__examples,
                                    examples_per_page=1, css=css)

        demo.launch()
