import numpy as np
import pandas as pd


class Mappings:

    def __init__(self, detections: pd.DataFrame):

        self.__detections = detections

    def intersects(self, instance: np.ndarray):

        # Are any of the <indices> within the range of the instance?
        ice = np.linspace(instance[0], instance[1], instance[1] - instance[0] + 1, dtype=int)
        conditionals = self.__detections['indices'].apply(lambda x: np.isin(x, ice).any())

        if sum(conditionals) == 0:
            return ''

        fract = self.__detections.copy().loc[conditionals, :]
        fract.sort_values(by='index', ascending=True, inplace=True)

        if fract['category'].unique().shape[0] == 1:
            return fract['entity'].values[0]
        else:
            return ''

    def exc(self):
        """

        :return:
        """

        # tag
        # np.apply_along_axis(func1d=intersects, axis=1, arr=page[['start', 'end']])

        # score
        # values = data.loc[0:5, 'score'].to_numpy()
        # values.prod()