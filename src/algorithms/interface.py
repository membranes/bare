"""Module interface.py"""
import logging

import src.algorithms.persist


class Interface:

    def __init__(self):
        """

        """

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)


    def exc(self, paragraph, summary, tokens):
        """

        :param paragraph:
        :param summary:
        :param tokens:
        :return:
        """

        self.__logger.info('paragraph: %s\n%s', type(paragraph), paragraph)
        self.__logger.info('summary: %s\n%s', type(summary), summary)
        self.__logger.info('tokens: %s\n%s', type(tokens), tokens)

        src.algorithms.persist.Persist().exc(paragraph=paragraph, tokens=tokens)
