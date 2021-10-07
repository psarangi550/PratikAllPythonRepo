import logging
import logging.config
import Dictlogger_config_file
logging.config.dictConfig(Dictlogger_config_file.logging_config)
# logger=logging.getLogger("demoLogger")
logger=logging.getLogger()#creating the root logger instead
logger.error("This is a Error File")