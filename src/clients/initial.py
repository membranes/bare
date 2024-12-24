"""Module initial.py"""

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

    def __init__(self, path: str):
        """

        :param path: The path to the underlying model's artefacts
        """

        self.__configurations = config.Config()

        # Pipeline
        self.__classifier = transformers.pipeline(task='ner', model=path, device=self.__configurations.device)

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

    def __custom(self, paragraph):
        """

        :param paragraph:
        :return:
        """

        tokens = self.__classifier(paragraph)
        table = self.__table(tokens=tokens)
        summary = {token['word']: [token['entity'], token['score']] for token in tokens}

        return {'text': paragraph, 'entities': tokens}, table, summary, tokens

    # noinspection PyTypeChecker
    def exc(self):
        """
        Despite the flagging mode message, 'auto' is a correct option and works as described;
        <a href="https://www.gradio.app/docs/gradio/interface" target="_blank">gradio.Interface()</a>.<br>

        :return:
        """

        css = ('.gradio-container-5-9-1 .prose table, .gradio-container-5-9-1 .prose tr, '
               '.gradio-container-5-9-1 .prose td, .gradio-container-5-9-1 .prose th '
               '{border:0 solid var(--body-text-color);}'
               '.paginate.svelte-p5q82i.svelte-p5q82i.svelte-p5q82i '
               '{justify-content:left; font-size:var(--text-md); margin-left: 10px;}')

        demo = gradio.Interface(
            self.__custom,
            inputs=gradio.Textbox(placeholder="Enter sentence here...", max_length=2000),
            outputs=[gradio.HighlightedText(interactive=False), 'html', 'json', gradio.Textbox()],
            examples=self.__configurations.examples, examples_per_page=1,
            title='Token Classification',
            description=('<b>An illustrative interactive interface; the interface '
                         'software allows for advanced interfaces.</b>'),
            flagging_mode='auto',
            css=css,
            stop_btn=gradio.Button('Stop', variant='stop', visible=True, interactive=False))

        demo.launch()
