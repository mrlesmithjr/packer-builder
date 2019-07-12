"""Set's up logging facility."""

import logging
from logging.handlers import TimedRotatingFileHandler
import os
import sys

FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = os.path.join('logs', 'builder.log')
if not os.path.isdir('logs'):
    os.makedirs('logs')


# Currently not implemented
def get_console_handler():
    """Sets up console logging handler."""
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler():
    """Sets up file logging handler."""
    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(logger_name):
    """Returns logger facility to module(s)."""
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    # logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = False
    return logger
