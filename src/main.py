"""Module main.py"""
import argparse
import glob
import logging
import os
import sys

import boto3
import torch


def main():
    """
    Entry Point

    :return:
    """

    logger: logging.Logger = logging.getLogger(__name__)

    # Set up
    setup: bool = src.setup.Setup(service=service, s3_parameters=s3_parameters).exc()
    if not setup:
        src.functions.cache.Cache().exc()
        sys.exit('No Executions')

    # ...
    if args.reacquire_artefacts:
        src.data.interface.Interface(service=service, s3_parameters=s3_parameters).exc()

    # Explore/Interact
    paths = glob.glob(os.path.join(root, 'data', '**', 'model'), recursive=True)
    src.algorithms.interface.Interface().exc(path=paths[0])

    # Delete Cache Points
    src.functions.cache.Cache().exc()


if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Activate graphics processing units
    os.environ['CUDA_VISIBLE_DEVICES']='0'
    os.environ['TOKENIZERS_PARALLELISM']='true'
    os.environ['HF_HOME']='/tmp'

    # Classes
    import src.algorithms.interface
    import src.data.interface
    import src.data.reacquire
    import src.functions.service
    import src.functions.cache
    import src.s3.s3_parameters
    import src.setup

    # Arguments
    reacquire = src.data.reacquire.Reacquire()
    parser = argparse.ArgumentParser()
    parser.add_argument('--reacquire', type=reacquire.reacquire_artefacts,
                        help=('Either True or False.  In answer to the question - '
                              'Should the model artefacts be reacquired?'))
    args = parser.parse_args()


    # S3 S3Parameters, Service Instance
    connector = boto3.session.Session()
    s3_parameters = src.s3.s3_parameters.S3Parameters(connector=connector).exc()
    service = src.functions.service.Service(connector=connector, region_name=s3_parameters.region_name).exc()

    main()
