import logging


def setup_logging(log_to_stdout=True, log_to_file=True):
    """
    Sets up logging configurations.

    Args:
        log_to_stdout (bool): Whether to log messages to stdout.
        log_to_file (bool): Whether to log messages to a file.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    if log_to_stdout:
        stdout_handler = logging.StreamHandler()
        stdout_handler.setFormatter(formatter)
        logger.addHandler(stdout_handler)

    if log_to_file:
        file_handler = logging.FileHandler('download.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
