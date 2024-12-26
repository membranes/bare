"""Module interface.py"""
import logging
import os

import src.algorithms.persist
import src.functions.objects
import src.settings.arguments


class Interface:
    """
    Executes the functions that process the input text, and the tokens classifications results.
    """

    def __init__(self, path: str):
        """

        :param path: The path to the underlying model's artefacts
        """

        objects = src.functions.objects.Objects()
        self.__architecture = objects.read(uri=os.path.join(os.path.dirname(path), 'architecture.json'))['name']
        self.__config = objects.read(uri=os.path.join(path, 'config.json'))

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __structuring(self):
        """
        In Progress

        :return:
        """

        match self.__architecture:
            case 'distil':
                self.__logger.info('proceed')
            case _:
                self.__logger.info('Unknown')

    def exc(self, paragraph, summary, tokens):
        """

        :param paragraph:
        :param summary:
        :param tokens:
        :return:
        """

        self.__logger.info(self.__architecture)
        self.__logger.info(self.__config)

        self.__logger.info('paragraph: %s\n%s', type(paragraph), paragraph)
        self.__logger.info('summary: %s\n%s', type(summary), summary)
        self.__logger.info('tokens: %s\n%s', type(tokens), tokens)

        self.__structuring()
        src.algorithms.persist.Persist().exc(paragraph=paragraph, tokens=tokens)
