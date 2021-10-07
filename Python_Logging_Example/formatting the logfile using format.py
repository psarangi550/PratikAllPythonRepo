#we can customize the format of details in the log file by using the format keyword argument
#basically while displaying the log it will always display in this default format
#:-1:-name of the logging level
#:-2:-name of the logger(root)by default
#3:-log messages which as passed as args while adding the data to the logfile
import logging#importing the logging module

logging.basicConfig(format="%(asctime)s:%(created)f:->%(lineno)d:%(levelno)s:%(name)s")#taking all the default value with only changing the format by format keyword args
print()
#here level name represent the logging level name
#here name represent the name of the logger
#here message will represent the log message wghich we try to print to the logfile
#as default value for filename=console,hence result will be displayed to the console
#as the default logging level is:-WARNING,hence warning and above level will added to the console
logging.critical("This is a Critical messages")
logging.error("This is a error messages")
# logging.warning("This is a warning messages")
logging.info("This is a info messages")
logging.debug("This is a debug messages")

#as we have only taken the level name and the name of the logger with name
#hence these 2 info will only be displayed to console
#but if we want to know few more details we can go visit python logging documentation
#using it for the python logging documentation few additional format
