#####################################
### CURRENT LOGGING EXAMPLES DEMO ###
#####################################

# Import logging set up
from ..logger import logger 

#Settings and meanings
#DEBUG = every step that has run 
#INFO = everything working as expected 
#WARNING = Something unexpected but still running
#ERROR = Something has failed
#CRITICAL = Something caused programme failiure.

### Example log messages ###

logger.debug("standard debug message") #not logged unless main/stdout logger level set to DEBUG.

logger.info("programme steps sucessfully completed") #not logged unless main/stdout logger level set to DEBUG.

logger.warning("unexpected finding during running but programme has completed") #prints to file.

logger.error("error during programme execution") #prints to stderr and file.

logger.critical("Unexpected critical error causing programme failiure") #prints to stderr and file.