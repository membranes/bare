"""Module cli.py"""
import logging

import transformers

import config


class CLI:
    """
    Command Line Interface
    """

    def __init__(self, path: str):
        """

        :param path: The path to the underlying model's artefacts
        """

        # Pipeline
        self.__classifier = transformers.pipeline(task='ner', model=path, device=config.Config().device)

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)30d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self, ):
        """

        :return:
        """

        # Sample Text
        sentence = input('A sentence please: ')

        # Re-print the input
        self.__logger.info('Sentence: %s', sentence)

        # Hence
        self.__logger.info(self.__classifier(sentence))
