#we can put the exception info the logfile as well by using the logging.exception(mesaages)just like other method
#here the default level for the exception is error level which is 50
#here our requirement is to input two number from the user and device in case of issue we can raise exception
#but everytime a request cam whether successful or error we want to see the log details
#fromn there we can see how many request came for this particular application
#howmany request out of them raised the exception
#how many of them are zero Division Error and how many of them are value error
import logging#importing the logging module

#as we are adding the log info before the user put the user input
#hence first the file will be create d then request will be initiate and the we can ask the user for two value
logging.basicConfig(filename="app.log",level=logging.DEBUG,filemode="a",format="%(asctime)s:%(levelname)s:%(name)s:%(message)s" , datefmt="%d:%m:%Y %I:%M:%S %p")
#one the log file being created by the basic Logging configuration
#we can ass for all the request a log message using the existing function
logging.info("A request just came in")
try:#riskey codei.e try with multiple except block
    x=int(input("Enter the first Number"))
    y=int(input("Enter the Second Number"))
    result=x/y
    print(f"The Answer of the division of {x} by {y} is {x/y}")
    logging.info(f"The Answer of the division is {x/y}")
except ZeroDivisionError as e:
    print(e.__class__.__name__)#handling code
    logging.exception("Can't devide by Zero")
except ValueError as e:
    print(e.__class__.__name__)#handling code
    logging.exception("Please Provide into value only")
#once everything sorted out then we can teell the logfile that request got completed
logging.info("Request Completed")

