"""Module interface.py"""
import logging
import os

import pandas as pd

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

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

        # Objects
        objects = src.functions.objects.Objects()

        self.__architecture = objects.read(uri=os.path.join(os.path.dirname(path), 'architecture.json'))['name']
        self.__logger.info(self.__architecture)

        self.__config = objects.read(uri=os.path.join(path, 'config.json'))
        self.__logger.info(self.__config)

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

    def exc(self, paragraphs: str, tokens: list):
        """

        :param paragraphs:
        :param tokens:
        :return:
        """

        sentences = paragraphs.splitlines()
        frame = pd.DataFrame(data={'sentence': sentences})
        self.__logger.info(sentences)
        self.__logger.info(frame)


        data = pd.DataFrame.from_records(data=tokens)
        data.sort_values(by='index', inplace=True)
        data.info()
        self.__logger.info(data)

        self.__structuring()

