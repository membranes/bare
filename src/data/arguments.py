import logging
import argparse

class Arguments:
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
        except ValueError:
            raise argparse.ArgumentTypeError(f'In answer to the question - Should the model artefacts be reacquired? - the '
                                             f'argument value must be either True or False')

        return status
