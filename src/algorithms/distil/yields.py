"""Module yields.py"""
import logging

import datasets
import pandas as pd
import transformers


class Yields:
    """
    Tokenization yields
    """

    def __init__(self, frame: pd.DataFrame, tokenizer: transformers.tokenization_utils_base.PreTrainedTokenizerBase):
        """

        :param frame:
        :param tokenizer:
        """

        self.__frame = frame
        self.__tokenizer = tokenizer

        # The critical fields
        self.__fields = ['words']

    def __features(self, blob: pd.DataFrame) -> pd.DataFrame:
        """

        :param blob:
        :return:
        """

        frame = blob.copy()
        frame['words'] = frame['sentence'].str.split()

        return frame[self.__fields]

    def __splittings(self):
        """

        :return:
        """

        splittings = datasets.DatasetDict({
            'latest': datasets.Dataset.from_pandas(
                self.__features(self.__frame))
        })

        return splittings

    def __tokenize(self, feeds):
        """

        :param feeds: sentence_identifier, words, codes
        :return:
        """

        logging.info(feeds['words'])

        # tokenization of words
        inputs = self.__tokenizer(feeds['words'], truncation=True, is_split_into_words=True)
        logging.info(inputs)

        return  inputs

    def exc(self) -> datasets.DatasetDict:
        """

        :return:
        """

        splittings = self.__splittings()
        logging.info(splittings)
        logging.info(splittings.keys())

        yields: datasets.DatasetDict = splittings.map(self.__tokenize, batched=True)

        return yields
