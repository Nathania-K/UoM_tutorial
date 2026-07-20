#####################################
### CONFIGURATION USED IN LOGGING ###
#####################################

#----------------------------------------#
# Step 0: Import required code settings  #
#----------------------------------------#

from pathlib import Path

#----------------------------------------#
# Step 1: Define default log file (in ~) #
#----------------------------------------#

LOG_DIRECTORY = "~/.SeqKit2026nk/logs"

# Logger Configuration
#home_dir = Path.home()
#DEFAULT_LOG = Path(home_dir, ".SeqKit2026nk/logs")

#LOG_FILE = DEFAULT_LOG

#---------------------------------------------#
# Step 2: Normalise the path (defensive step) #
#---------------------------------------------#

#LOG_FILE = Path(LOG_FILE).expanduser().resolve()
