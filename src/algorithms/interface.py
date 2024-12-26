"""Module interface.py"""
import logging
import os
import glob

import config
import src.algorithms.persist
import src.functions.objects
import src.settings.arguments
import src.elements.s3_parameters as s3p


class Interface:

    def __init__(self, path: str, s3_parameters: s3p.S3Parameters):
        """

        :param path:
        :param s3_parameters:
        """

        uri = os.path.join(os.path.dirname(path), 'architecture.json')
        objects = src.functions.objects.Objects()
        self.__architecture = objects.read(uri=uri)['name']

        # Arguments
        self.__arguments = src.settings.arguments.Arguments(
            s3_parameters=s3_parameters).exc(architecture=self.__architecture)

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

        self.__logger.info(self.__architecture)
        self.__logger.info(self.__arguments)

        self.__logger.info('paragraph: %s\n%s', type(paragraph), paragraph)
        self.__logger.info('summary: %s\n%s', type(summary), summary)
        self.__logger.info('tokens: %s\n%s', type(tokens), tokens)

        src.algorithms.persist.Persist().exc(paragraph=paragraph, tokens=tokens)
