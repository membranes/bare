"""Module interface.py"""
import logging
import typing

import src.clients.basic
import src.clients.cli
import src.clients.future
import src.clients.initial


class Interface:
    """
    Offers interaction interfaces.
    """

    def __init__(self):
        """

        Constructor
        """

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
                src.clients.future.Future().exc()
            case 'initial':
                src.clients.initial.Initial().exc()
            case _:
                return 'Unknown'
