import logging #importing the logging module
import logging.config#importing the logging.config in order to load the file into the application by fileConfig("file location")
logging.config.fileConfig("logging_config.init")#loading the logfile configuration into the application
#then we nee to create a logger with getLogger("logger object vwe written to the file")
logger=logging.getLogger("demologger")#creating the logging object so that we can write the logger object and add the data to the logfile
logger.critical("This is a Critical Message")