"""Module initial.py"""
import os

import gradio
import transformers

import config


class Initial:
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

    def __custom(self, paragraph):
        """

        :param paragraph:
        :return:
        """

        tokens = self.__classifier(paragraph)
        summary = {token['word']: [token['entity'], token['score']] for token in tokens}

        return {'text': paragraph, 'entities': tokens}, summary, tokens

    # noinspection PyTypeChecker
    def exc(self):
        """
        Despite the flagging mode message, 'auto' is a correct option and works as described;
        <a href="https://www.gradio.app/docs/gradio/interface" target="_blank">gradio.Interface()</a>.<br>

        :return:
        """

        demo = gradio.Interface(
            self.__custom,
            inputs=gradio.Textbox(placeholder="Enter sentence here...", max_length=2000),
            outputs=[gradio.HighlightedText(interactive=False), 'json', gradio.Textbox()],
            examples=self.__configurations.examples, examples_per_page=1,
            title='Token Classification',
            description=('<b>An illustrative interactive interface; the interface '
                         'software allows for advanced interfaces.</b>'),
            flagging_mode='auto')

        demo.launch(server_port=7860)
