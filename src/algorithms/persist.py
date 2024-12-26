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

    @staticmethod
    def exc(paragraph: str, tokens: list):
        """

        :param paragraph: The input text
        :param tokens:
        :return:
        """

        logging.info(paragraph)

        data = pd.DataFrame.from_records(data=tokens)
        data.sort_values(by='index', inplace=True)
        data.info()
        logging.info(data.head(n=33))
