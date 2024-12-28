"""Module interface.py"""
import logging
import os

import config
import src.algorithms.detections
import src.algorithms.mappings
import src.algorithms.page
import src.functions.objects


class Interface:
    """
    Executes the functions that process the input text, and the tokens classifications results.
    """

    def __init__(self):
        """
        Constructor
        """

        self.__configurations = config.Config()

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

    def exc(self, text: str, tokens: list):
        """

        :param text:
        :param tokens:
        :return:
        """

        m_config = self.__m_config()

        page = src.algorithms.page.Page(text=text).exc()
        detections = src.algorithms.detections.Detections(tokens=tokens).exc(m_config=m_config)
        mappings = src.algorithms.mappings.Mappings(page=page, detections=detections).exc(m_config=m_config)

        self.__logger.info('Page:\n%s', page)
        self.__logger.info('Detections:\n%s', detections)
        self.__logger.info('Mappings:\n%s', mappings)
