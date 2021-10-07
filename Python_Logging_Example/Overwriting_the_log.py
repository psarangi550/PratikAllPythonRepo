#if we want to to overwrite the default append nature to overwrite nature then we have to use the another keyword args as filemode
#filemode="w":-overwrite mode and log message will be over written
#filemode:-"a":-appending to the existing log file
#here we are using the over write mode
#we can take any extension for the log file abc.txt or abc.log everything is fine
import logging#importing the logging module

logging.basicConfig(filename="abc..txt",level=logging.DEBUG,filemode="w")
print("Basic configuration Happened Successfully")#here printing to the console
logging.critical("This is a Critical Log File")
logging.error("This is a error Log File")
logging.warning("This is a warning Log File")
logging.info("This is a info Log File")
logging.debug("This is a debug Log File")