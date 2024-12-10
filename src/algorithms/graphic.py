import logging
import transformers
import gradio


class Graphic:

    def __init__(self, path: str):
        """

        :param path: The model's path
        """

        self.__examples = [
            'The English writer and the Afghani soldier.',
            'It was written by members of the United Nation.',
            ('There were more than a hundred wolves in the Tiger Basin.  It is a dangerous place '
            'after 9 p.m., especially near Lake Victoria.')
        ]

        # Pipeline
        self.__classifier = transformers.pipeline(task='ner', model=path, device='cuda')
        logging.info(self.__classifier)

    def __table(self, tokens) -> str:

        head = ('<table style="width: 55%; font-size: 65%; text-align: left;">'
                '<colgroup>'
                '<col span="1" style="width: 15%;"><col span="1" style="width: 15%;"><col span="1" style="width: 15%;">'
                '</colgroup>'
                '<thead><tr><th>word</th><th>entity</th><th>score</th></tr></thead>')

        for token in tokens:
            head = head + f"<tr><td>{token['word']}</td><td>{token['entity']}</td><td>{token['score']}</td></tr>"

        head = head + '</table>'

        return head


    def __basic(self, paragraph):
        """

        :param paragraph:
        :return:
        """

        outcome = self.__classifier(paragraph)

        return {'text': paragraph, 'entities': outcome}

    def __custom(self, paragraph):

        tokens = self.__classifier(paragraph)

        highlight = []
        for token in tokens:
            highlight.extend([(token['word'], token['entity']), (' ', None)])
        logging.info(highlight)

        summary = {token['word']: [token['entity'], token['score']] for token in tokens}
        logging.info(summary)

        return {'text': paragraph, 'entities': tokens}, summary

    def exc(self, basic: bool = True):

        if basic:
            demo = gradio.Interface(self.__basic,
                                    gradio.Textbox(placeholder="Enter sentence here..."),
                                    gradio.HighlightedText(),
                                    examples=self.__examples)
        else:
            demo = gradio.Interface(self.__custom,
                                    gradio.Textbox(placeholder="Enter sentence here..."),
                                    [gradio.HighlightedText(), 'json'],
                                    examples=self.__examples)

        demo.launch()
