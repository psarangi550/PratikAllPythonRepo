#here in this case we will built 4 different custom logger
#1:-Only with StreamHandler:-which can be done with the root logger as well using the default value of the file name which is console
#2nd one we will try on the file Handler which can be done with default logger or root logger
#3rd one:-we will try on the both in my way and durgas's way which is not possible with default logger as default logger only support
#one file handler can act at a time as the once the basic logging config declared for the root logger then it became final we can't add or remove the basic config explicitly
#if we force try it will not be considered
#one logging level can be set which is the base Logging config level will be considered
#we can only use 1 log file at the moment won't provide support for handling multiple log file,as the basic logging config file configuration will be considered and the other once ruled out
#but the caveat over here is the messages of later basic config will be added to first basic level configuration
#the 5th one we will see how to operate on 2 different module with custom logger
#lets get started
#we will be providing each definition for the step



#in order to create the custom logger we need 5 step
# first step :->to create a custom logger object :-which will implement custom logging
#in order to do we have to use
import logging#importing the logging module
#creating the custom logger obejct with the help the getLogger()
#getLogger() take the name of the logger  as string and return the logger object
logger=logging.getLogger("PratikLogger")
#by default the logging level for the logger is NOT SET(0)
#if we want tot set that then we have to use setLogger(logging.CRITICAL/ERROR/WARNING/DEBUG/INFO) on the logger object
#this way we can se the logging label for the logger
logger.setLevel(logging.DEBUG)#setting the label as Debug
#2nd step:->we need to create a Handler for the custom logger whose main responsibility is to handle which and how log message will be displayed to the custom logger log files
#here we need to create the Handler object
#there are multiple types of handler are there
#SteamHandler class (for console)/FileHandler Class (for logfile )/SMTPHandler( for email)/HTTPHandler(HTTP Protocol log to the web server)
#creating the object of stream Handler() Handler object
consoleHandler=logging.StreamHandler()#creating the object for the sream Handler class
#on the next example we will discuss about the file Handler,where we can take the mode as well whether append or overwrite
#for the fileHandler the default logging level is ===logging label of logger
#if we want to set it explicitly then also it will be considered
#if we want to set the level the at runtime Handler Level will be considered  rather than Logger
consoleHandler.setLevel(logging.INFO)#setting the handler logging level as info
#so info and higher will be considered while writing the log to the logfile
#rememebr that we can add multiple handler for the same custom logger which option is not available in the case of root logger
#step:-3:-creating the formatter object in which format logg message will be displayed to the console
#formatter took the message format whch need to be displayed to the console somehow similar to format keyword args in the case of default logger
formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s",datefmt="%d:%m:%Y %H:%M:%S %p")
#creating the formatter object by the help of formatter function which take
#step:-4:-setting the formatter object to the handler so that handler have the complete info for the log message
#for setting the formatter to the handler object we need to use the setFormatter(Formatter object) as below
#on the handler object we need to call the setFormatter object
consoleHandler.setFormatter(formatter)
#Step:-5:-adding the handler the logger so that we can display the log files with custom logger
#here we need to use the addHandler(Handler Object) on the logger object
logger.addHandler(consoleHandler)
#step:-6:-
#now we can be able to add the data to the log file using the inbuilt function
#but here instead of module we need to call by the logger object
logger.critical("This is a Critical Message")
logger.error("This is a error Message")
logger.warning("This is a warning Message")
logger.info("This is a Info Message")
logger.debug("This is a Debug Message")