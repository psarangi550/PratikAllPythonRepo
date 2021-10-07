import logging
import Problem_with_root_logger_part_1
logging.basicConfig(filename="pratik.txt",level=logging.DEBUG,filemode="w")
logging.critical("This is critical message of Test module")
logging.error("This is critical message of Test module")
logging.warning("This is critical message of Test module")
logging.info("This is critical message of Test module")
logging.debug("This is critical message of Test module")