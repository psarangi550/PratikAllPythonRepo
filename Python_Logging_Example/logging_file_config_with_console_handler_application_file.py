import logging
import sys
import logging.config
logging.config.fileConfig("logging_file_config_console.init")
logger=logging.getLogger("demologger1")
logger.critical("This is a critical Message")