"""Module interface.py"""
import sys

import dask

import src.data.artefacts
import src.elements.s3_parameters as s3p
import src.elements.service as sr
import src.s3.directives
import src.s3.unload


class Interface:
    """
    Notes<br>
    ------<br>

    An interface to the data/artefacts retrieval class.  <b>Beware, sometimes dask
    will be unnecessary, edit accordingly.</b>
    """

    def __init__(self, service: sr.Service, s3_parameters: s3p.S3Parameters):
        """

        :param service: A suite of services for interacting with Amazon Web Services.
        :param s3_parameters: The overarching S3 (Simple Storage Service) parameters
                              settings of this project, e.g., region code name, buckets, etc.
        """

        self.__service: sr.Service = service
        self.__s3_parameters: s3p.S3Parameters = s3_parameters
        self.__source_bucket = self.__s3_parameters.external

        # Directives
        self.__directives = src.s3.directives.Directives()

    @dask.delayed
    def __get_assets(self, source_bucket: str, origin: str, target: str):
        """

        :param source_bucket:
        :param origin:
        :param target:
        :return:
        """

        return self.__directives.synchronise(
            source_bucket=source_bucket, origin=origin, target=target)

    def exc(self):
        """

        :return:
        """

        # Get the artefacts metadata; the prefix is the string between
        # a bucket name and one or more key names, herein it starts and ends without a stroke, i.e., /.
        strings = src.data.artefacts.Artefacts(
            service=self.__service).exc(source_bucket=self.__source_bucket, prefix='warehouse/numerics/best/model')

        # Compute
        computation = []
        for origin, target in zip(strings['source'], strings['destination']):
            state = self.__get_assets(source_bucket=self.__source_bucket, origin=origin, target=target)
            computation.append(state)
        executions: list[int] = dask.compute(computation, scheduler='threads')[0]

        if all(executions) == 0:
            return True

        sys.exit('Artefacts download step failure.')
