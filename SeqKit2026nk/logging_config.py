#####################################
### DICTCONFIG SETUP FOR  LOGGING ###
#####################################

#----------------------------------------#
# Step 0: Import required code settings  #
#----------------------------------------#

from pathlib import Path

#----------------------------------------#
# Step 1: Define default log file (in ~) #
#----------------------------------------#

LOG_DIR = Path("~/.SeqKit2026nk/logs").expanduser()
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Logger Configuration
LOG_FILE = LOG_DIR / "app_log.log"

#---------------------------------------------#
# Step 4: Logging.configuration.              #
#---------------------------------------------#
LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    
    "formatters": {
        "standard": {
            "format": ("%(asctime)s - %(levelname)-8s - %(name)s - "
            "%(filename)s - %(message)s"
            )
        }
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard"
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "filename": LOG_FILE
        },
    },

    "loggers": {
        "SeqKit2026nk": {
            "level": "INFO",
            "handlers": ["console", "file"],
            "propagate": False,
        },
    },

    "root": {
        "level": "DEBUG",
        "handlers": ["console", "file"],
    }
}