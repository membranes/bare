"""Module artefacts.py"""
import logging
import os

import numpy as np
import pandas as pd

import config
import src.elements.service as sr
import src.s3.prefix


class Artefacts:
    """
    The artefacts per architecture
    """

    def __init__(self, service: sr.Service):
        """

        :param service: A suite of services for interacting with Amazon Web Services.
        """

        self.__service = service

        # Configurations
        self.__configurations = config.Config()

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __keys(self, source_bucket: str, prefix: str) -> list:
        """

        :return:
        """

        listings: list = src.s3.prefix.Prefix(
            service=self.__service, bucket_name=source_bucket).objects(prefix=prefix)

        return listings

    def __strings(self, sources: np.ndarray):
        """

        :param sources: An array of Amazon S3 (Simple Storage Service) prefixes
        :return:
        """

        # A data frame consisting of the S3 keys ...
        frame = pd.DataFrame(data={'source': sources})

        # ... and local storage area.  For the local storage area, ensure that the
        # appropriate directory separator is in place.
        frame = frame.assign(destination=frame['source'])
        frame = frame.assign(destination=frame['destination'].replace(to_replace='/', value=os.path.sep))
        frame = frame.assign(destination=self.__configurations.data_ + os.path.sep + frame['destination'])

        return frame

    def exc(self, source_bucket: str, prefix: str) -> pd.DataFrame:
        """
        Determining the unique segments of a prefix.  Remember, a prefix is the string between
        a bucket name and a key name; starts and ends without a stroke, i.e., /.

        :param source_bucket:
        :param prefix:
        :return:
        """

        # The keys within the prefix
        keys = self.__keys(source_bucket=source_bucket, prefix=prefix)

        # Hence, the distinct paths
        sources = np.array([os.path.dirname(k) for k in keys])
        sources = np.unique(sources)
        self.__logger.info(sources)

        # Source & Destination
        strings = self.__strings(sources=sources)
        self.__logger.info(strings)

        return strings
