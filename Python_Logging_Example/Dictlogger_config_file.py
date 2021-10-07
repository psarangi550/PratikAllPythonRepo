import logging#importing the logging module
logging_config=dict(version=1,
                    formatters={"f":{"format":"%(asctime)s:%(levelname)s:%(name)s:%(message)s",
                                     "datefmt":"%d:%m:%Y %I:%M:%S %p"
                                    }},
                    handlers={"h":{"class":"logging.StreamHandler",
                                   "level":logging.DEBUG,
                                   "formatter":"f",
                                   }},
                    root={"level":logging.DEBUG,
                                     "handlers":["h"]},
                    demoLogger={"level":logging.DEBUG,
                                     "handlers":["h"]}
                    )
