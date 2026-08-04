import logging

logger = logging.getLogger(__name__)


def prompt_to_continue():
    """
    Allows user to continue or exit program
    """
    #Creates infinite loop with message until user input results in a True/False return
    while True:
        logger.info("Press Enter to continue or Q to quit")

        try:
            response = input().strip().lower()
        except (KeyboardInterrupt, EOFError):
            logger.info("Program cancelled by user.")
            return False

        if response == "":
            return True #returning True allows program to continue.

        if response in {"q", "quit"}:
            logger.info("Program cancelled by user.")
            return False

        #Raised if anything other than "", "q" or "quit" is returned.
        logger.warning("Invalid input: Enter Q to quit or press Enter to continue.")



def request_block_line_integer (name, default):
    """ 
    Requests positive integer for block_size and blocks_per_line.
    Pressing 'enter' returns the specified default settings.
    """

    while True:
        logger.info(
            "Enter %s, press Enter for %d, or type 'q' to quit.",
            name,
            default,
        )

        try:
            response = input().strip().lower()
        except (KeyboardInterrupt, EOFError):
            logger.info("formatting selection cancelled by user.")
            return None

        if response in {"q", "quit"}:
            logger.info ("formatting selection cancelled by user.")
            return None

        if response == "":
            return default

        try:
            value = int(response)
        except ValueError:
            logger.warning (
                "%s must be a whole number. Please enter a value above 0.",
                name,
            )
            continue

        if value <= 0: 
            logger.warning("%s must be greater than 0.", name)
            continue

        return value