import logging 

logger = logging.getLogger(__name__)

def user_dna_sequence():
    """
    Cleans user input for downstream GenBank conversion
    """

    allowed_characters = set("actgnx")
    
    while True:
        
        try: user_sequence = input()
        except (KeyboardInterrupt, EOFError):
            logger.info("sequence entry cancelled.")
            return None #Feeds back into main() def to cancel program 

        #cleans input = remove any inputted whitespace and convert to lowercase (if required).
        sequence = "".join(user_sequence.split()).lower()

        #checks cleaned sequence is empty and warns of invalid input, returns to input sequence if false.
        if not sequence:
            logger.warning("No sequence entered: Please enter DNA sequence.")
            continue

        invalid_characters = set(sequence) - allowed_characters

        if invalid_characters:
            invalid = ", ".join(sorted(invalid_characters))

            #presents invalid characters to user if previously entered in sequence and restates valid characters.
            logger.warning("Invalid characters in sequence '%s'", invalid)
            logger.info("only A, C, T, G, N and X characters permitted. Please enter a valid DNA sequence.")
            continue

        logger.info("DNA sequence received")

        return sequence
