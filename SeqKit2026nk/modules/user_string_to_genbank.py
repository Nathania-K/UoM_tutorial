#definition to allow user input (with conversion from caps to lowercase)
import logging
from datetime import datetime
from pathlib import Path
from SeqKit2026nk.logger import setup_logging
from SeqKit2026nk.utils.util_mods import prompt_to_continue 
from SeqKit2026nk.utils.util_mods import request_integer

#set logger for this module
logger = logging.getLogger(__name__)



def main():
    """
    Takes user input DNA sequence and converts into GenBank format on default settings.
    If custom formatting used, sequence is formatted as specified by user.
    """

    #Inital start of program prompting user to input DNA sequence into console.
    logger.info("Step 1: DNA sequence entry.")
    sequence = user_dna_sequence()

    if sequence is None:
        logger.info("Program cancelled by user.")
        return

    logger.info ("DNA sequence accepted.")

    if not prompt_to_continue():
        return

    #Format DNA sequence into specified/default settings.
    logger.info("Step 2: Format DNA sequence.")

    formatting_settings = request_format_settings()

    if formatting_settings is None:
        return

    block_size, blocks_per_line = formatting_settings

    formatted_sequence = user_format_sequence(
        sequence,
        block_size=block_size,
        blocks_per_line=blocks_per_line,
    )

    if formatted_sequence is None:
        return

    logger.info("DNA sequence successfully formatted.")

    if not prompt_to_continue():
        return

    logger.debug(
        "Program completed - formatted sequence is now: \n%s",
        formatted_sequence,
    )

    filename = choose_filename()

    if filename is None:
        return 

    output_file = save_formatted_sequence(
        formatted_sequence,
        filename,
    )


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
            logger.info("only A, C, T, G, N and X characters permitted.")
            continue

        logger.info("DNA sequence received")

        return sequence



def request_format_settings(
    default_block_size=10,
    default_blocks_per_line=6,
):
    """
    Collects user formatting settings and returns tuple with both values or None if cancelled.
    Cancelling will return None.
    Uses request_block_line_integer() function in util.mod for 
    """

    block_size = request_integer(
        "block size",
        default_block_size,
    )

    if block_size is None:
        return None

    blocks_per_line = request_integer(
        "blocks per line",
        default_blocks_per_line,
    )

    if blocks_per_line is None:
        return None 

    return block_size, blocks_per_line



def user_format_sequence (sequence, block_size=10, blocks_per_line=6):
    """
    Takes cleaned sequence from user_dna_sequence and creates GenBank format (using 3 parameters).
    Custom format settings taken from tuple produced in request_format_settings().
    Default format settings retained if no block/line integer provided.
    """

    #Prevents user entering empty sequence
    if not sequence:
        logger.warning("cannot format empty sequence.")
        return None

    #Prevents user entering 0 params if specified when calling function individually.
    if block_size <= 0 or blocks_per_line <= 0:
        logger.error("Invalid formatting values: block_size and blocks_per_line must be greater than 0.")
        return None

    logger.debug(
        "formatting sequence of %d bases into blocks of %d.",
        len(sequence),
        block_size,
    )

    bases_per_line = block_size * blocks_per_line 
    lines = [] 

    #starts loop through every 60 bases
    for start in range(0, len(sequence), bases_per_line): 
        #ensures line start defined every specified bases (i.e. default = 0:60, 60:120, 120:180)
        line_sequence = sequence[start:start + bases_per_line]

        blocks = []

        #loops through line sequence in specified-base blocks (i.e. default line = 0, 10, 20, 30, 40, 50)
        for index in range(0, len(line_sequence), block_size): 
            block = line_sequence[index:index + block_size] #extracts one block of 10 bases.
            blocks.append(block)

        #creates GenBank format with corrected line position, right-aligned (9 chars) and joins blocks with space.
        lines.append(f"{start + 1:>9} {' '.join(blocks)}") 

    formatted_sequence = "\n".join(lines) #converts list into single string.

    logger.info(
        "formatted %d bases into %d lines.",
        len(sequence),
        len(lines),
    )

    return formatted_sequence #Note: GenBank format in lowercase technically correlates to RNA (DNA is always uppercase).



def choose_filename(): 
    """
    Allows user to choose filename.
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



def save_formatted_sequence(
    formatted_sequence,
    filename="formatted_sequence.txt" 
    ):
    """ 
    Saves GenBank formatted sequence to output folder in parent directory (UOM_Tutorials).
    If OSError (i.e. due to unexpected format), returns None and no file saved.
    """ 
    #Gets and sets the project directory (UOM_Tutorial) path and attaches 'output' file
    project_dir = Path(__file__).resolve().parents[2]
    output_dir = project_dir / "outputs"
    output_file = output_dir / filename

    #creates the directory (or parent directories if missing) and prevents error if exists.
    try:
        output_dir.mkdir(parents=True, exist_ok=True)

        output_file.write_text(
            formatted_sequence + "\n", #adds new line after formatted sequence.
            encoding="utf-8" #specifies how text is encoded.
        )

    except OSError as error:
        logger.error ("Could not save sequence as %s", error)
        return None 

    logger.info("Formatted sequence saved to %s", output_file)
    return output_file



if __name__ == "__main__":
    setup_logging()
    main()
