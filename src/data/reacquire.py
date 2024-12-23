import argparse

class Reacquire:
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
    def reacquire_artefacts(value: str = False) -> bool:
        """

        :param value: Either True or False.  In answer to the question - Should the model
                      artefacts be reacquired?
        :return:
        """

        try:
            status = bool(value.capitalize())
        except ValueError as err:
            raise argparse.ArgumentTypeError(f'In answer to the question - Should the model artefacts be reacquired? - the '
                                             f'argument value must be either True or False')

        return status
