#definition to allow user input (with conversion from caps to lowercase)
import logging
from SeqKit2026nk.logger import setup_logging


#set logger for this module
logger = logging.getLogger(__name__)

def main():
    logger.info("Step 1: DNA sequence entry")
    sequence = user_dna_sequence()

    if sequence is None:
        logger.info("Program cancelled by user")
        return

    if not prompt_to_continue(
        "DNA sequence accepted"
        ):
        return

    logger.info("Step 2: Format DNA sequence")

    formatted_sequence = user_format_sequence(sequence)

    if not prompt_to_continue(
        "DNA sequence successfully converted to GenBank formatting"
    ):
        return

    logger.debug(
        "Program completed: GenBank format is: \n%s",
        formatted_sequence,
    )


#Create definition to ensure correct user entry for downstream GenBank conversion
def user_dna_sequence():
    allowed_characters = set("actg")
    
    #when input matches allowed characters
    while True:
        logger.info("Enter a DNA sequence: ")
        
        try: user_sequence = input()
        except (KeyboardInterrupt, EOFError):
            logger.info("sequence entry cancelled.")
            return None

        #cleans input = remove any inputted whitespace and convert to lowercase (if required).
        sequence = "".join(user_sequence.split()).lower()

        #checks cleaned sequence is empty and warns of invalid input, returns to input sequence if false.
        if not sequence:
            logger.warning("No sequence entered/wrong sequence format")
            continue

        invalid_characters = set(sequence) - allowed_characters

        if invalid_characters:
            invalid = ", ".join(sorted(invalid_characters))

            logger.warning("Invalid characters in sequence %s", invalid)
            logger.info("only A, C, T and G characters permitted")
            continue

        logger.info("DNA sequence received")

        return sequence


#Takes cleaned sequence from user_dna_sequence and creates GenBank format (using 3 parameters).
def user_format_sequence (sequence, block_size=10, block_per_line=6):
    if not sequence:
        logger.warning("cannot format empty sequence")
        return ""

    if block_size <= 0 or block_per_line <= 0:
        logger.error("Invaid formatting values: block_size and blocks_per_line must be greater than 0")
        return

    logger.debug(
        "formatting sequence of %d bases into blocks of %d.",
        len(sequence),
        block_size,
    )

    bases_per_line = block_size * block_per_line 
    lines = [] 

    for start in range(0, len(sequence), bases_per_line): #Loops through 60-base steps.
        line_sequence = sequence[start:start + bases_per_line]

        blocks = []

        #loops through line sequence in 10-base blocks (i.e. full line = 0, 10, 20, 30, 40, 50)
        for index in range(0, len(line_sequence), block_size): 
            block = line_sequence[index:index + block_size] #extracts one block of 10 bases.
            blocks.append(block)

        #creates completed format with correct zero position, right aligned (9 chars) and joins blocks with space.
        lines.append(f"{start + 1:>9} {' '.join(blocks)}") 

    formatted_sequence = "\n".join(lines) #converts list into single string.

    logger.info(
        "formatted %d bases into %d lines",
        len(sequence),
        len(lines),
    )

    return formatted_sequence

def prompt_to_continue(message):
    while True:
        logger.info("%s", message)
        logger.info("Press Enter to continue or Q to quit")

        try:
            response = input().strip().lower()
        except (KeyboardInterrupt, EOFError):
            logger.info("Program cancelled by user.")
            return False

        if response == "":
            return True

        if response in {"q", "quit"}:
            logger.info("Program cancelled by user.")
            return False

        logger.warning("Enter Q to quit or press Enter to continue.")

if __name__ == "__main__":
    setup_logging()
    main()