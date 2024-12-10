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
            'It was written by members of the United Nation.'
        ]

        # Pipeline
        self.__classifier = transformers.pipeline(task='ner', model=path)
        logging.info(self.__classifier)

    def ner(self, paragraph):
        """

        :param paragraph:
        :return:
        """

        outcome = self.__classifier(paragraph)

        return {'text': paragraph, 'entities': outcome}

    def custom(self, paragraph):

        tokens = self.__classifier(paragraph)

        highlight = []
        for token in tokens:
            highlight.extend([(token['word'], token['entity']), (' ', None)])
        logging.info(highlight)

        summary = {token['word']: [token['entity'], token['score']] for token in tokens}
        logging.info(summary)

        return {'text': paragraph, 'entities': tokens}, summary

    def exc(self, spare: bool = True):

        if spare:
            demo = gradio.Interface(self.ner,
                                    gradio.Textbox(placeholder="Enter sentence here..."),
                                    gradio.HighlightedText(),
                                    examples=self.__examples)
        else:
            demo = gradio.Interface(self.custom,
                                    gradio.Textbox(placeholder="Enter sentence here..."),
                                    [gradio.HighlightedText(), 'json'],
                                    examples=self.__examples)

        demo.launch()
