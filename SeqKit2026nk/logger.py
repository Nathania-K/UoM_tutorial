import logging.config

from SeqKit2026nk.logging_config import LOG_CONFIG

#Apply logging configuration.abs

def setup_logging():
    logging.config.dictConfig(LOG_CONFIG)