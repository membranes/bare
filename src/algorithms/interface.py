"""Module interface.py"""
import logging
import os
import random
import string

import config
import src.algorithms.detections
import src.algorithms.mappings
import src.algorithms.page
import src.functions.objects
import src.functions.streams


class Interface:
    """
    Executes the functions that process the input text, and the tokens classifications results.
    """

    def __init__(self):
        """
        Constructor
        """

        self.__configurations = config.Config()
        self.__streams = src.functions.streams.Streams()

        # Characters space
        self.__characters = string.ascii_lowercase + string.digits + string.ascii_uppercase

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __m_config(self) -> dict:
        """

        :return:
        """

        objects = src.functions.objects.Objects()
        uri = os.path.join(self.__configurations.data_, 'model', 'config.json')

        return objects.read(uri=uri)

    def __path(self) -> str:
        """

        :return:
        """

        name = ''.join(random.choices(self.__characters, k=23))

        return  os.path.join(self.__configurations.interactions_, f'{name}.csv')

    def exc(self, text: str, tokens: list):
        """

        :param text:
        :param tokens:
        :return:
        """

        # The underlying model's configuration dictionary.
        m_config = self.__m_config()

        # The input text
        page = src.algorithms.page.Page(text=text).exc()
        self.__logger.info('Page:\n%s', page)

        # The detections
        detections = src.algorithms.detections.Detections(tokens=tokens).exc(m_config=m_config)
        self.__logger.info('Detections:\n%s', detections)

        # Hence, map
        mappings = src.algorithms.mappings.Mappings(page=page, detections=detections).exc(m_config=m_config)
        self.__logger.info('Mappings:\n%s', mappings)

        # Save
        self.__streams.write(blob=mappings, path=self.__path())
