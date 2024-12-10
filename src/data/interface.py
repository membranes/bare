import json
import logging

import src.elements.s3_parameters as s3p
import src.elements.service as sr
import src.s3.unload

import src.data.artefacts
import src.s3.directives


class Interface:

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

    def __get_dictionary(self, key_name: str) -> dict:
        """
        s3:// {bucket.name} / {key.name}

        :param key_name: prefix, file name, file extension
        :return:
        """

        buffer = src.s3.unload.Unload(s3_client=self.__service.s3_client).exc(
            bucket_name=self.__s3_parameters.external, key_name=key_name)
        dictionary = json.loads(buffer)

        return dictionary

    def exc(self):


        key_name = 'warehouse/numerics/best/architecture.json'
        dictionary = self.__get_dictionary(key_name=key_name)
        logging.info(dictionary['name'])

        # Get the artefacts metadata
        strings = src.data.artefacts.Artefacts(
            service=self.__service, s3_parameters=self.__s3_parameters).exc(architecture=dictionary['name'])

        # Retrieve the artefacts
        states = src.s3.directives.Directives(s3_parameters=self.__s3_parameters).exc(
            source=strings['source'], destination=strings['destination'])
        self.__logger.info(states)
