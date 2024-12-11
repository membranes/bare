"""config.py"""
import os


class Config:
    """
    Config
    """

    def __init__(self) -> None:
        """
        Constructor<br>
        -----------<br>

        Variables denoting a path - including or excluding a filename - have an underscore suffix; this suffix is
        excluded for names such as warehouse, storage, depository, etc.<br><br>
        """

        self.warehouse = os.path.join(os.getcwd(), 'warehouse')
        self.data_ = os.path.join(os.getcwd(), 'data')
        self.artefacts_ = os.path.join(self.data_, 'artefacts')

        # Amazon
        self.s3_parameters_key = 's3_parameters.yaml'
        self.architecture_key = 'warehouse/numerics/best/architecture.json'
