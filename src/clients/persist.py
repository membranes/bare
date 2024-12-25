"""Module persist.py"""
import logging

import pandas as pd


class Persist:
    """
    Save
    """

    def __init__(self):
        """
        Constructor
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

        data = pd.DataFrame.from_records(data=tokens)
        data.sort_values(by='index', inplace=True)
        data.info()
        self.__logger.info(data.head(n=33))
