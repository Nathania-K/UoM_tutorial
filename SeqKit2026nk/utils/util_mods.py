import logging
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)


def choose_filename(prefix="formatted_sequence"):
    """
    Allows user to choose filename for a .txt file.
    Prefix used when generating the default timestamped filename.
    Pressing enter will generate defaulted filename (current date/time). 
    Returns None if cancelled.
    """

    #Sets up timestamp and default filename(+timestamp) if default filename selected.
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    default_filename = f"{prefix}_{timestamp}.txt"

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
        if Path(filename).suffix.lower() != ".txt":
            filename += ".txt"

        return filename


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


def request_integer(name, default):
    """ 
    Requests positive integer for block_size and blocks_per_line.

    Pressing 'enter' returns the specified default settings.
    Entering 'q' or cancelling returns None
    """

    #Asks user to enter a custum number or Enter to get defaulted settings in request_format_settings() or quit.
    while True:
        logger.info(
            "Enter %s, press Enter for %d, or type 'q' to quit.",
            name,
            default,
        )

        #cleans the input of whitespaces and puts input into lowercase.
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

        #accepts only integers as a reponse and returns warning anything else provided.
        try:
            value = int(response)
        except ValueError:
            logger.warning (
                "%s must be a whole number. Please enter a value above 0.",
                name,
            )
            continue
        
        #Ensures that interger entered must be over 0. 
        if value <= 0: 
            logger.warning("%s must be greater than 0.", name)
            continue

        return value


def request_yes_no(message="would you like to continue?"):
    """
    Requests a 'Yes/No' response from user.
    Returns True for 'Yes' and False for 'No'.
    """

    #Opens loop to ask if user would like to continue. Message customisable but will default to above message if not supplied.
    while True:
        logger.info("%s", message)

        try:
            response = input().strip().lower()
        except (KeyboardInterrupt, EOFError):
            logger.info("Program cancelled by user.")
            return False

        if response in {"y", "yes"}:
            logger.debug ("Continuing.")
            return True 

        if response in {"n", "no"}:
            logger.debug ("Request cancelled by user.")
            return False

        logger.warning("Invalid response - please eneter 'Y' to continue or 'N' to cancel.")

