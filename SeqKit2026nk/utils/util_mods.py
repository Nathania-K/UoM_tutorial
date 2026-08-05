import logging
from datetime import datetime
from pathlib import Path

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


def choose_filename(): 
    """
    Allows user to choose filename for a .txt file.
    Pressing enter will generate defaulted filename (current date/time). 
    Returns None if cancelled.
    """

    #Sets up timestamp and default filename(+timestamp) if default filename selected.
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    default_filename = f"formatted_sequence_{timestamp}.txt"

    while True:
        logger.info(
            "Enter an output file, "
            "press enter for %s, or Q to quit",
            default_filename,
        )

        try: 
            filename = input().strip()
        except (KeyboardInterrupt, EOFError):
            logger.info("Filename entry cancelled by user.")
            return None

        #if 'q' or 'quit' is entered (case insensitive), file save is cancelled.
        if filename.lower() in {"q", "quit"}:
            logger.info(
                "filename entry cancelled by user."
                )
            return None

        #Pressing enter returns default filename.
        if filename == "":
            return default_filename

        #If path is entered, user reprompted for filename without directory path.
        if Path(filename).name != filename:
            logger.warning(
                "Filename cannot include path, please enter name of file only."
                )
            continue

        #Adds '.txt' to filename end if not added previously.
        if Path(filename).suffix == "":
            filename += ".txt"

        return filename


def request_integer (name, default):
    """ 
    Requests positive integer for block_size and blocks_per_line.

    Pressing 'enter' returns the specified default settings.
    Entering 'q' or cancelling returns None
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