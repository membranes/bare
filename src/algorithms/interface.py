"""Module interface.py"""
import logging

import config
import src.algorithms.cli
import src.algorithms.graphic



class Interface:
    """
    Offers interaction interfaces.
    """

    def __init__(self):
        """
        Constructor
        """

        self.__configurations = config.Config()

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
            src.algorithms.cli.CLI().exc(path=path)

        self.__logger.info('Via Interface: ')
        src.algorithms.graphic.Graphic(path=path).exc(basic=False)
