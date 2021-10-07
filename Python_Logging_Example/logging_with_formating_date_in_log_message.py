#here for formatting the date and time we need 2 things
#1st one is:-=>in the format keyword args we must have "%(asctime)s" parameter value in the basicConfig()
#and we can amend the date and time format by using the datefmt keyword args
#here in the datefmt keyword args we need to take %d:-date %m-:-month %Y:-year in 4 digit format
#here we need to take %H:-Hours in 24 hours format %M:-minutes format %S:-seconds
#for am or PM:-we need to to keep it as %p
#there are few more which can be searched from python documentation
import logging#importing the logging module

logging.basicConfig(filename="xyz.txt",level=logging.DEBUG,filemode="w",format="%(asctime)s:%(levelname)s:%(name)s:%(message)s",datefmt='%d:%m:%Y %I:%M:%S %p')
#addding the date and time format which will over ride the default timedate format which created by asctime parameter in format keyword args
logging.critical("This is a Critical Message")
logging.error("This is a error Message")
logging.warning("This is a warning Message")
logging.info("This is a info Message")
logging.debug("This is a debug Message")