import os
import logging

import pandas as pd

import config
import src.algorithms.distil.yields
import src.algorithms.distil.tokenizer

import src.functions.objects


class Steps:

    def __init__(self):
        """
        Constructor
        """

        objects = src.functions.objects.Objects()

        # Model
        self.__config = objects.read(uri=os.path.join(config.Config().data_, 'model', 'config.json'))
        self.__tokenizer = (src.algorithms.distil.tokenizer.Tokenizer(
            pretrained_model_name_or_path=self.__config['_name_or_path']).__call__())

    def exc(self, frame: pd.DataFrame):
        """

        :param frame:
        :return:
        """

        yields = src.algorithms.distil.yields.Yields(
            frame=frame, tokenizer=self.__tokenizer)

        objects = yields.exc()

        logging.info(objects.keys())
