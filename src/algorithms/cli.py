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

        self.__configurations = config.Config()

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)30d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self, path: str):
        """
        'The English writer and the Afghani soldier, both live in Algeria.'

        :return:
        """

        # Sample Text
        paragraph = input('A sentence please: ')
        self.__logger.info(paragraph)

        # Pipeline
        classifier = transformers.pipeline(task='ner', model=path, device='cuda')
        self.__logger.info(classifier)

        # Hence
        self.__logger.info(classifier(paragraph))
