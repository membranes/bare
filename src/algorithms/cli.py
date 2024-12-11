"""Module cli.py"""
import logging

import transformers

import config


class CLI:
    """
    Command Line Interface
    """

    def __init__(self):
        """
        Constructor
        """

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)30d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self, path: str):
        """

        :return:
        """

        # Sample Text
        sentence = input('A sentence please: ')
        self.__logger.info('Sentence: %s', sentence)

        # Pipeline
        classifier = transformers.pipeline(task='ner', model=path, device=config.Config().device)

        # Hence
        self.__logger.info(classifier(sentence))
