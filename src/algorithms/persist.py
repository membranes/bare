"""Module persist.py"""
import os
import time

import datasets

import config
import src.functions.directories


class Persist:
    """
    Save
    """

    def __init__(self):
        """
        Constructor
        """

        self.__configurations = config.Config()

        self.__directories = src.functions.directories.Directories()

    def exc(self, blob: datasets.Dataset):
        """

        :param blob:
        :return:
        """

        # A path name via current time
        segment: int = int(time.time())
        path = os.path.join(self.__configurations.warehouse, f'{segment}')

        # Create the path
        self.__directories.create(path=path)

        # Save
        blob.save_to_disk(dataset_path=path)
