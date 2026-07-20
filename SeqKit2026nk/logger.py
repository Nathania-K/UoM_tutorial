import logging
import sys
from logging import handlers
from pathlib import Path 

from .logging_config import LOG_DIRECTORY

# Create a logger instance
logger = logging.getLogger("SeqKit_logger")
logger.setLevel(logging.DEBUG) #can modify log level here - DEBUG|INFO|WARNING|ERROR|CRITICAL
logger.propagate = False

# Prevent duplicate handlers if imported multiple times
if not logger.handlers:

    #find project route
    current_dir = Path(__file__).resolve().parent
    project_dir = Path(current_dir).parent.resolve()

    #create logs directory if not previously existed
    log_dir = Path(LOG_DIRECTORY).expanduser()
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / "app_log.log"

    # Create a formatter
    formatter = logging.Formatter("%(asctime)s - %(levelname)-8s - %(name)s - %(filename)s - %(message)s")

    # Create a handler for console/terminal (Error/Critical messages)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG) #sets the desired level for stderr
    console_handler.setFormatter(formatter)

    # Create a rotating file handler (warning|error|critical - max 500kb and 5x backups)
    file_handler = handlers.RotatingFileHandler(
        log_file,
        maxBytes=500_000,
        backupCount=5,
    ) 

    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(formatter) 

    # Add the handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
