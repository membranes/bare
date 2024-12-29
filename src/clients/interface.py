"""Module interface.py"""
import logging
import typing

import src.clients.basic
import src.clients.cli
import src.clients.future
import src.clients.initial
import src.elements.s3_parameters as s3p
import src.elements.service as sr


class Interface:
    """
    Offers interaction interfaces.
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
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)30d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self, client: typing.Literal['basic', 'cli', 'future', 'initial'] = 'future'):
        """

        :param client: A client via which to interact with the model.
        :return:
        """

        self.__logger.info('Trying: %s', client)

        match client:
            case 'basic':
                src.clients.basic.Basic().exc()
            case 'cli':
                src.clients.cli.CLI().exc()
            case 'future':
                src.clients.future.Future(service=self.__service, s3_parameters=self.__s3_parameters).exc()
            case 'initial':
                src.clients.initial.Initial().exc()
            case _:
                return 'Unknown'
