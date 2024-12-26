"""Module arguments.py"""

import pandas as pd

import src.elements.arguments
import src.elements.s3_parameters as s3p


class Arguments:
    """
    Arguments<br>
    ---------<br>

    Reads-in a JSON (JavaScript Object Notation) file of arguments
    """

    def __init__(self, s3_parameters: s3p.S3Parameters):
        """

        :param s3_parameters: s3_parameters: The overarching S3 (Simple Storage Service) parameters
                              settings of this project, e.g., region code name, buckets, etc.
        """

        self.__s3_parameters = s3_parameters

    def __get_dictionary(self, architecture: str):
        """
        s3:// {bucket.name} / ... / {key.name}

        :param architecture:
        :return:
        """

        path = 's3://' + self.__s3_parameters.configurations + f'/architecture/{architecture}/' + 'arguments.json'

        try:
            values = pd.read_json(path_or_buf=path, orient='index')
        except ImportError as err:
            raise err from err

        return values.to_dict()[0]

    def exc(self, architecture: str) -> src.elements.arguments.Arguments:
        """

        :param architecture:
        :return:
        """

        # Get the dictionary of arguments
        dictionary = self.__get_dictionary(architecture=architecture)

        # A model output directory placeholder
        dictionary['model_output_directory'] = ''

        return src.elements.arguments.Arguments(**dictionary)
