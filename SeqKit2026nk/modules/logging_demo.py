#####################################
### CURRENT LOGGING EXAMPLES DEMO ###
#####################################

#Settings and meanings
#DEBUG = every step that has run 
#INFO = everything working as expected 
#WARNING = Something unexpected but still running
#ERROR = Something has failed
#CRITICAL = Something caused programme failiure.

# Import logging set up

import logging

logger = logging.getLogger(__name__)

def logging_demo():

    logger.debug("standard debug message") #saves to file

    logger.info("programme started successfully") #saves to file

    logger.warning("Unexpected finding during running but continuing") #saves to file

    logger.error("Something failed during programme execution") #saves to file

    logger.critical("Serious error, programme may fail") #saves to file

    logger.info("Demo complete, check console and file log") 

    return None

if __name__ == '__main__':
    logging_demo()