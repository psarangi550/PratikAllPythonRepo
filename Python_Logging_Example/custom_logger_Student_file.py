import logging#importing the logging module
#now we want to write to a logfile lets say student.txt
#we can also set the file mode as append and format with date and time along with log levelname and name of the logger but with out log messages
logger=logging.getLogger("StudentLogger")#creating the logger object
#setting the label as DEBUG for the logger which is same for the handler
logger.setLevel(logging.DEBUG)#setting the lavel for the logger which is default for the handler
#now we can add the Handler to it
fileHandler=logging.FileHandler("Student.txt")#calling the FileHandler Class object to create that FileHandler
#now creating the formatter with ate and time along with log levelname and name of the logger but with out log messages
formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s" , datefmt="%d:%m:%Y %H:%M:%S %p")
#setting the formatter to the handler
fileHandler.setFormatter(formatter)
#now adding the handler to the logger
logger.addHandler(fileHandler)
logger.critical("This is Critical Message")
logger.error("This is Error Message")
logger.warning("This is Warning Message")
logger.info("This is info Message")
logger.debug("This is debug Message")
