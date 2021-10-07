#here we need to import the logger first
from logging import *
from cust_logger.get_cust_logger import *
def m1():
    logger=getLogger(ERROR,"w")
    logger.critical("This is a Critical Message")
    logger.error("This is a Error Message")
m1()#calling the test_logger function