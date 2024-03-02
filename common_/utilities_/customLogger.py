from pathlib import Path
import logging
import os
from datetime import datetime


def _get_root_directory():
    """
        Get the root directory of the project based on the current file's location.
    """
    try:
        projectName = "amazon_automation"
        currentPath = Path(__file__)
        projectRootPath = Path((str(currentPath).split(projectName))[0]) / projectName

        return projectRootPath

    except FileNotFoundError as e:
        logger("ERROR", f"Error: The directory was not found: {str(e)}")
        exit(6)
    except Exception as e:
        logger("ERROR", f"Error: An unexpected error occurred: {str(e)}")
        exit(5)


def logger(level, message, fileName=os.path.join(_get_root_directory(), 'logs_', f'log_{datetime.now().strftime("%d_%m_%Y_%H-%M-%S")}.log')):
    """
        Log messages at different log levels (INFO, DEBUG, WARNING, ERROR, CRITICAL) with exception handling.
    """
    try:
        logging.basicConfig(level=logging.INFO, filename=fileName, filemode="a",
                            format="%(asctime)-12s %(levelname)s %(message)s",
                            datefmt="%d-%m-%Y %H:%M:%S")

        if level == "INFO":
            logging.info(message)
        elif level == "DEBUG":
            logging.debug(message)
        elif level == "WARNING":
            logging.warning(message)
        elif level == "ERROR":
            logging.error(message)
        elif level == "CRITICAL":
            logging.critical(message)
    except Exception as e:
        logger("ERROR", f"Error: An error occurred while logging: {str(e)}")
        exit(7)
