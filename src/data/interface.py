"""Module interface.py"""
import json
import logging

import config
import src.data.artefacts
import src.elements.s3_parameters as s3p
import src.elements.service as sr
import src.s3.directives
import src.s3.unload


class Interface:
    """
    Interface
    """

    def __init__(self, service: sr.Service, s3_parameters: s3p.S3Parameters):
        """

        :param service: A suite of services for interacting with Amazon Web Services.
        :param s3_parameters: The overarching S3 (Simple Storage Service) parameters
                              settings of this project, e.g., region code name, buckets, etc.
        """

        self.__service: sr.Service = service
        self.__s3_parameters: s3p.S3Parameters = s3_parameters

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __get_architecture(self, key_name: str) -> str:
        """
        s3:// {bucket.name} / {key.name}

        :param key_name: prefix, file name, file extension
        :return:
        """

        buffer = src.s3.unload.Unload(s3_client=self.__service.s3_client).exc(
            bucket_name=self.__s3_parameters.external, key_name=key_name)
        dictionary = json.loads(buffer)

        return dictionary['name']

    def exc(self):
        """

        :return:
        """

        architecture = self.__get_architecture(key_name=config.Config().architecture_key)
        logging.info('The best model, named by its underlying architecture: %s', architecture)

        # Get the artefacts metadata
        strings = src.data.artefacts.Artefacts(
            service=self.__service, s3_parameters=self.__s3_parameters).exc(architecture=architecture)

        # Retrieve the artefacts
        messages = src.s3.directives.Directives(s3_parameters=self.__s3_parameters).exc(
            source=strings['source'], destination=strings['destination'])
        self.__logger.info(messages)
