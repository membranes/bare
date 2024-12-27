"""Module interface.py"""
import logging
import os

import pandas as pd

import config
import src.functions.objects
import src.settings.arguments
import src.algorithms.distil.steps


class Interface:
    """
    Executes the functions that process the input text, and the tokens classifications results.
    """

    def __init__(self):
        """
        Constructor
        """

        # Objects
        objects = src.functions.objects.Objects()
        self.__architecture = objects.read(
            uri=os.path.join(config.Config().data_, 'architecture.json'))['name']

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)



    def __structuring(self, frame: pd.DataFrame):
        """
        In Progress

        :return:
        """

        match self.__architecture:
            case 'distil':
                self.__logger.info('%s ...', self.__architecture)
                src.algorithms.distil.steps.Steps().exc(frame=frame)
            case _:
                self.__logger.info('Unknown')

    def exc(self, paragraphs: str, tokens: list):
        """

        :param paragraphs:
        :param tokens:
        :return:
        """

        data = pd.DataFrame.from_records(data=tokens)
        data.sort_values(by='index', inplace=True)
        data.info()
        self.__logger.info(data)


        frame = pd.DataFrame(data={'sentence': [paragraphs]})
        self.__logger.info(paragraphs)
        self.__logger.info(frame)
        self.__structuring(frame=frame)
