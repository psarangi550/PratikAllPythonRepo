#here if we need to add the both Handler we can do that which is not possible with the root logger
#here we will also can take different different logging level for the logger
import logging#iomporting the logging module
logger=logging.getLogger("demoLogger")
#creating the logger object
logger.setLevel(logging.DEBUG)#setting the level as debug
#now creating the handler Object
#here we arte creating 2 different Handler object
consoleHandler=logging.StreamHandler()#creating the object of Stream handler in here
fileHandler=logging.FileHandler("demo.txt",mode="w")#creating the object of FileHandler with filename and file mode as argument
#now we can create formatter object we can even create 2 different formatter object where the format being different
formatter1=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s", datefmt="%d:%m:%Y %I:%M:%S %p")
formatter2=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s", datefmt="%d:%m:%Y %H:%M:%S %p")
#we can set these different formatter for the different Handler
consoleHandler.setFormatter(formatter1)
fileHandler.setFormatter(formatter2)
#now we have to add both the handler to the logger
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)
#now we can write the data to the custom logger
logger.critical("This is a Critical Message")
logger.error("This is a Error Message")
logger.warning("This is a warning Message")
logger.info("This is a Info Message")
logger.debug("This is a Debug Message")