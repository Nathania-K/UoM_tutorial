import logging.config
from SeqKit2026nk.logging_config import LOG_CONFIG
from SeqKit2026nk.logger import setup_logging
from SeqKit2026nk.modules.logging_demo import logging_demo

def main():
    setup_logging()
    logging_demo()

if __name__ == "__main__":
    main()