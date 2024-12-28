import logging
import typing

import numpy as np
import pandas as pd


class Mappings:

    def __init__(self, page: pd.DataFrame, detections: pd.DataFrame):
        """

        :param page: The input text page in data frame form.  The text has been split into words; each
                     instance represents a word.
        :param detections: The non-miscellaneous tokens detected by the model.
        """

        self.__page = page
        self.__detections = detections

    def __intersects(self, instance: np.ndarray):
        """

        :param instance: Part of an instance of self.__page.  It consists of an instance's
                         word start index [0], and word end index [1]
        :return:
        """

        # Do any of the tokens of self.__detections classify this instance?
        indices_of_instance = np.linspace(instance[0], instance[1], instance[1] - instance[0] + 1, dtype=int)
        conditionals = self.__detections['indices'].apply(lambda x: np.isin(x, indices_of_instance).any())

        return conditionals

    def __instances(self, conditionals) -> typing.Tuple[pd.DataFrame, int]:
        """

        :param conditionals:
        :return:
        """

        instances = self.__detections.copy().loc[conditionals, :]
        instances.sort_values(by='index', ascending=True, inplace=True)

        # The distinct categories
        n_categories = instances['category'].unique().shape[0]

        return instances, n_categories

    def __tag(self, instance: np.ndarray) -> str:
        """

        :param instance:
        :return:
        """

        conditionals = self.__intersects(instance=instance)
        logging.info(conditionals)

        if sum(conditionals) == 0:
            return ''

        instances, n_categories = self.__instances(conditionals=conditionals)

        if n_categories == 1:
            return instances['entity'].values[0]
        else:
            return ''

    def __score(self, instance: np.ndarray) -> float:
        """

        :param instance:
        :return:
        """

        conditionals = self.__intersects(instance=instance)
        logging.info(conditionals)

        if sum(conditionals) == 0:
            return np.nan

        instances, n_categories = self.__instances(conditionals=conditionals)

        if n_categories == 1:
            return instances['score'].to_numpy().prod()
        else:
            return np.nan

    def exc(self):
        """

        :return:
        """

        data = self.__page.copy()
        data['tag'] = np.apply_along_axis(func1d=self.__tag, axis=1, arr=data[['start', 'end']])
        data['score'] = np.apply_along_axis(func1d=self.__score, axis=1, arr=data[['start', 'end']])
