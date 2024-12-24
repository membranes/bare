"""Module future.py"""
import logging

import gradio
import transformers

import config


class Future:
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

        self.__css = ('.gradio-container-5-9-1 .prose table, .gradio-container-5-9-1 .prose tr, '
                      '.gradio-container-5-9-1 .prose td, .gradio-container-5-9-1 .prose th '
                      '{border:0 solid var(--body-text-color);}'
                      '.paginate.svelte-p5q82i.svelte-p5q82i.svelte-p5q82i '
                      '{justify-content:left; font-size:var(--text-md); margin-left: 10px;}')

    def __custom(self, paragraph):
        """

        :param paragraph:
        :return:
        """

        tokens = self.__classifier(paragraph)
        summary = {token['word']: [token['entity'], token['score']] for token in tokens}

        return {'text': paragraph, 'entities': tokens}, summary, tokens

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
                    compact = gradio.Textbox(label='compact')

            gradio.ClearButton([paragraph, detections, scores, compact])
            detect.click(self.__custom, inputs=paragraph, outputs=[detections, scores, compact])
            gradio.Examples(examples=self.__configurations.examples, inputs=[paragraph], examples_per_page=1)

        demo.launch()
