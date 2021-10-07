import logging#importing the logging module
#here we need to create a basic Logging configuration using the  log file and logging level
#loggiong module has basic config function which will implement logging
#logging.basicConfig(filename="file location of the log file",level=logging.AnyLevel)
#default value of :-level:-Warning
#by default:-Append will going to happen
#by default :-if no file name it will be written to the console
#if we want tot write the data to the logfile there are multiple methods
#logging.critical(message)
#logging.error(message)
#logging.warning(message)
#logging.info(message)
#logging.debug(message)
#file extension can be anything
#if the file is not present the it will create the new file
#if present then appending operation will going to happen not the overWriting
#as its appending everytime we are executing the details will be added to the file
logging.basicConfig(filename="abc.log",level=logging.WARNING)
#here level and file name are the keyword args and parameter value
print("Basic config successful")
logging.critical("This is critical message")
logging.error("This is critical message")
logging.warning("This is critical message")
logging.info("This is critical message")
logging.debug("This is critical message")
#as the level set as warning hence warning and above level dat will be added ignoring the info and debug
