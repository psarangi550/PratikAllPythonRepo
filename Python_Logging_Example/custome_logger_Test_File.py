#here we want to import the  file custom_logger_Student_file to add the logs to 2 different log file with different logging level
import logging#importing the logging module
import custom_logger_Student_file
logger=logging.getLogger("TestLogger")
logger.setLevel(logging.WARNING)
#now creating the file Handler with Test.txt with over write mode
fileHandler=logging.FileHandler("Test.txt",mode="w")#creating the file Handler
#now creating the formatter object
formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s",datefmt="%d:%m:%Y %H:%M:%S %p")
#now we need to set the formatter to the Handler
fileHandler.setFormatter(formatter)
#we cam add the Handler to the logger
logger.addHandler(fileHandler)
#now we can write the log tot the logfile with cutomized logger
logger.critical("This is a Critical message")
logger.error("This is a error message")
logger.warning("This is a warning message")
logger.info("This is a info message")
logger.debug("This is a debug message")