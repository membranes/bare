"""Module variables.py"""
import logging
import argparse

class Variables:
    """
    Note<br>
    ------<br>

    A temporary approach to re-acquiring the model artefacts, if necessary, from
    Amazon S3 (Simple Storage Service).  This predominantly for the interface
    development phase.

    """

    def __init__(self):
        pass

    @staticmethod
    def reacquire(value: str) -> bool:
        """

        :param value: Either True or False.  In answer to the question - Should the model
                      artefacts be reacquired?
        :return:
        """

        logging.info('Latest: %s', value)

        try:
            status = bool(value.capitalize())
        except ValueError as err:
            raise argparse.ArgumentTypeError('In answer to the question - Should the model artefacts be reacquired? - the '
                                             'argument value must be either True or False') \
                from err

        return status
