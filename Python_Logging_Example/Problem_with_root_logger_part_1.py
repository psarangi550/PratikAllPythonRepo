import logging#importing the logging moduile
def main():
    logging.basicConfig()#add the default format
    logging.critical("This is critical message of student module")
    logging.error("This is critical message of student module")
    logging.warning("This is critical message of student module")
    logging.info("This is critical message of student module")
    logging.debug("This is critical message of student module")
if __name__=="__main__":
    main()
    
