"""Module cli.py"""
import logging
import os

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

        self.__configurations = config.Config()

        # Pipeline
        self.__classifier = transformers.pipeline(
            task='ner', model=os.path.join(self.__configurations.data_, 'model'),
            device=config.Config().device)

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
