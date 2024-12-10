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

    def exc(self):
        demo = gradio.Interface(self.ner,
                                gradio.Textbox(placeholder="Enter sentence here..."),
                                gradio.HighlightedText(),
                                examples=self.__examples)

        demo.launch()
