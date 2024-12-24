"""Module interface.py"""
import logging

import src.clients.cli
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

    def exc(self, path: str, cli: bool = False):
        """

        :param path: The model's path
        :param cli: Explore via command line interface?
        :return:
        """

        if cli:
            self.__logger.info('Via CLI: ')
            src.clients.cli.CLI().exc(path=path)

        self.__logger.info('Via Interface: ')
        src.clients.initial.Initial(path=path).exc(basic=False)
