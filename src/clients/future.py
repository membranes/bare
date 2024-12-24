"""Module future.py"""
import logging

import gradio
import transformers

import config


class Illustration:
    """
    A set-up that allows for custom interface options.
    """

    def __init__(self, path: str):
        """

        :param path: The path to the underlying model's artefacts
        """

        self.__configurations = config.Config()

        # Pipeline
        self.__classifier = transformers.pipeline(task='ner', model=path, device=self.__configurations.device)

        self.__css = ('.gradio-container-5-8-0 .prose table, .gradio-container-5-8-0 .prose tr, '
                      '.gradio-container-5-8-0 .prose td, .gradio-container-5-8-0 .prose th '
                      '{border:0 solid var(--body-text-color);}'
                      '.paginate.svelte-p5q82i.svelte-p5q82i.svelte-p5q82i '
                      '{justify-content:left; font-size:var(--text-md); margin-left: 10px;}')

    def __custom(self, paragraph):
        """

        :param paragraph:
        :return:
        """

        tokens = self.__classifier(paragraph)
        logging.info(tokens)
        summary = {token['word']: [token['entity'], token['score']] for token in tokens}

        return {'text': paragraph, 'entities': tokens}, summary

    @staticmethod
    def __selection():
        """
        Notes<br>
        -------<br>

        <b>Objective</b>: The wherewithal to click on a highlighted text and correct its tag assignment if it
        is incorrect.  Subsequently, the corrected piece is saved in alongside the original results; opt
        for a smart saving option.<br><br>

        def onselect(event: gradio.SelectData): return event.index.<br>
        .select(onselect, inputs=None, outputs=options)<br><br>

        :return:
        """

        gradio.Dropdown(
            ['O', 'B-GEO', 'B-GPE', 'B-TIM', 'B-ORG', 'I-GEO', 'B-PER', 'I-PER', 'I-ORG', 'I-TIM', 'I-GPE'],
            interactive=True, label='tags')

    def exc(self):
        """

        :return:
        """

        with gradio.Blocks(css=self.__css) as demo:

            gradio.Markdown(value=('<h1>Token Classification</h1><br><b>An illustrative interactive interface; the interface '
                                   'software allows for advanced interfaces.</b>'), line_breaks=True)

            with gradio.Row():
                with gradio.Column():
                    paragraph = gradio.Textbox(label='paragraph', placeholder="Enter sentence here...")
                    detect = gradio.Button(value='Submit')
                with gradio.Column():
                    detections = gradio.HighlightedText(label='detections', interactive=True)
                    scores = gradio.JSON(label='scores')

            gradio.ClearButton([paragraph, detections, scores])
            detect.click(self.__custom, inputs=paragraph, outputs=[detections, scores])
            gradio.Examples(examples=self.__configurations.examples, inputs=[paragraph], examples_per_page=1)

        demo.launch()
