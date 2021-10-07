import inspect#importing the inspect module
import logging#importing the logging module
from logging import *
def getLogger(level,mode):
    logger_name=inspect.stack()[1][3]
    logger=logging.getLogger(logger_name)
    logger.setLevel(level)
    fileHandler=logging.FileHandler(f"{logger_name}.txt",mode=mode)
    formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s",datefmt="%A:%B:  %d:%m:%Y %I:%M:%S %p")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger
