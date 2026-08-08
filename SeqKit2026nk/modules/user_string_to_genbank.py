#definition to allow user input (with conversion from caps to lowercase)
import logging
from SeqKit2026nk.logger import setup_logging

from SeqKit2026nk.utils.util_mods import prompt_to_continue, choose_filename, request_yes_no

from SeqKit2026nk.modules.user_dna_sequence import user_dna_sequence
from SeqKit2026nk.modules.user_format_sequence import user_format_sequence
from SeqKit2026nk.modules.request_format_settings import request_format_settings
from SeqKit2026nk.modules.save_formatted_sequence import save_formatted_sequence
from SeqKit2026nk.modules.transcribe_to_rna import transcribe_to_rna

#set logger for this module
logger = logging.getLogger(__name__)


def main():
    """
    Takes user input DNA sequence and converts into GenBank format on default settings.
    If custom formatting used, sequence is formatted as specified by user.
    """

    #STEP 1: Request DNA sequence from user into console.
    logger.info("Step 1: DNA sequence entry.")
    sequence = user_dna_sequence()

    if sequence is None:
        logger.info("Program cancelled by user.")
        return

    logger.info ("DNA sequence accepted.")

    if not prompt_to_continue():
        return

    #STEP 2: Formats DNA sequence into specified/default settings.
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

    #STEP 3: Choose whether to save formatted sequence into a custom/default file.
    dna_filename = choose_filename("formatted_dna")

    if dna_filename is None:
        return 

    output_file = save_formatted_sequence(
        formatted_sequence,
        dna_filename,
    )

    if output_file is None:
        return

    logger.info("File saved as %s", output_file)

    #STEP 4: Ask user if they wish to convert to RNA.
    logger.info("Would you like to convert to RNA?")

    if not request_yes_no("Press 'Y' to convert to RNA or 'N' to cancel"):
        return 

    formatted_rna_sequence = transcribe_to_rna(formatted_sequence)

    if formatted_rna_sequence is None:
        return output_file

    logger.info("formatted RNA sequence: \n%s", formatted_rna_sequence)

    #STEP 5: Ask if user wants to save RNA file.
    logger.info("Would you like to save the formatted RNA sequence?")

    if not request_yes_no("Press 'Y' to save file or 'N' to cancel"):
        return output_file
        
    rna_filename = choose_filename("formatted_rna")

    if rna_filename is None:
        return 

    output_rna_file = save_formatted_sequence(
        formatted_rna_sequence,
        rna_filename,
    )

    if output_rna_file is None:
        return output_file

    return output_rna_file

if __name__ == "__main__":
    setup_logging()
    main()
