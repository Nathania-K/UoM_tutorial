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