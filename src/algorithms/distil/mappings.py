import numpy as np
import pandas as pd
import typing


class Mappings:

    def __init__(self, page: pd.DataFrame, detections: pd.DataFrame):
        """

        :param page: The input text page in data frame form.  The text has been split into words; each
                     instance represents a word.
        :param detections: The non-miscellaneous tokens detected by the model.
        """

        self.__detections = detections

    def __intersects(self, instance: np.ndarray):
        """

        :param instance:
        :return:
        """

        # Are any of the <indices> within the range of the instance?
        ice = np.linspace(instance[0], instance[1], instance[1] - instance[0] + 1, dtype=int)
        conditionals = self.__detections['indices'].apply(lambda x: np.isin(x, ice).any())

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

    def __tag(self, conditionals) -> str:

        if sum(conditionals) == 0:
            return ''

        instances, n_categories = self.__instances(conditionals=conditionals)

        if n_categories == 1:
            return instances['entity'].values[0]
        else:
            return ''

    def __score(self, conditionals) -> float:

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

        # tag
        # np.apply_along_axis(func1d=intersects, axis=1, arr=page[['start', 'end']])

        # score
        # values = data.loc[0:5, 'score'].to_numpy()
        # values.prod()