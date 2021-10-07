#here in this we need to take care of the custome logger for the fileHandler
#which is exaclty same with obnly one change
#here the handler need to created by
#logging.FileHandler("filename",mode="w/a")
#like this we cann the file handler
#lets get started for this one
import logging#importing the logging module
#creating the logger object and this time i am not setting any level
logger=logging.getLogger("RikaLogger")#creating the custom logger object to implement logging
#creating the handler object and here also i don't want to set any level
fileHandler=logging.FileHandler("rika.log",mode="a")#creating thr object of FileHandler class with file name and file mode as parameter
#here setting the mode by the help of mode keyword args for the root logger it is filemode
#now creating the formatter object
formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s", datefmt="%d:%m:%Y %H:%M:%S %p")#creating the object of the Formatter class
#setting the formatter for the handler
fileHandler.setFormatter(formatter)
#adding the handler to the logger
logger.addHandler(fileHandler)
#now we can ass the later info wilth the hjelp of logger object instead of logging module which is for the root logger
logger.critical("This is a Critical Message")
logger.error("This is a error Message")
logger.warning("This is a warning Message")
logger.info("This is a Info Message")
logger.debug("This is a Debug Message")