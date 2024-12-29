"""Module dictionary.py"""
import glob
import os

import numpy as np
import pandas as pd


class Dictionary:
    """
    Class Dictionary
    """

    def __init__(self):
        """
        Constructor
        """

        # Metadata
        self.__metadata = {
            'start': 'The starting index of a word, in relation to a text.',
            'word': 'A word of a text.',
            'end': 'The ending index of a word, in relation to a text.',
            'code_of_tag_p': 'The identification code of the predicted tag.',
            'score': 'A score denoting how sure the model is about the tag it assigned to the word.  Maximum 1, minimum 0.',
            'tag_p': 'The predicted tag of the word.'}

    @staticmethod
    def __local(path: str, extension: str) -> pd.DataFrame:
        """

        :param path: The path wherein the files of interest lie
        :param extension: The extension type of the files of interest
        :return:
        """

        splitter = os.path.basename(path) + os.path.sep

        # The list of files within the path directory, including its child directories.
        files: list[str] = glob.glob(pathname=os.path.join(path, '**', f'*.{extension}'),
                                     recursive=True)

        if len(files) == 0:
            return pd.DataFrame()

        details: list[dict] = [
            {'file': file,
             'vertex': file.rsplit(splitter, maxsplit=1)[1],
             'section': os.path.basename(os.path.dirname(file))}
            for file in files]

        return pd.DataFrame.from_records(details)

    def exc(self, path: str, extension: str, prefix: str) -> pd.DataFrame:
        """

        :param path: The path wherein the files of interest lie
        :param extension: The extension type of the files of interest
        :param prefix: The Amazon S3 (Simple Storage Service) where the files of path are heading
        :return:
        """

        local: pd.DataFrame = self.__local(path=path, extension=extension)

        if local.empty:
            return pd.DataFrame()

        # Building the Amazon S3 strings
        frame = local.assign(key=prefix + local["vertex"])

        # The metadata dict strings
        frame['metadata'] = np.array(self.__metadata).repeat(frame.shape[0])

        return frame[['file', 'key', 'metadata']]
