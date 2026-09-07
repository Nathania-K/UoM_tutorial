#definition to allow user input (with conversion from caps to lowercase)
import logging
from SeqKit2026nk.logger import setup_logging

from SeqKit2026nk.utils.util_mods import prompt_to_continue, choose_filename, request_yes_no

from SeqKit2026nk.modules.user_dna_sequence import user_dna_sequence
from SeqKit2026nk.modules.user_format_sequence import user_format_sequence
from SeqKit2026nk.modules.request_format_settings import request_format_settings
from SeqKit2026nk.modules.save_formatted_sequence import save_formatted_sequence
from SeqKit2026nk.modules.transcribe_to_rna import transcribe_to_rna
from SeqKit2026nk.modules.translate_rna import translate_rna

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


    #STEP 2: Formats DNA sequence into specified/default settings.
    logger.info("Step 2: Format DNA sequence.")

    if not prompt_to_continue():
        return

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

    logger.debug(
        "formatted sequence is now: \n%s",
        formatted_sequence,
    )

    if not prompt_to_continue():
        return


    #STEP 3: Optional save of formatted sequence into a custom/default file.
    output_dna_file = None

    logger.info("Save formatted DNA sequence?")

    if request_yes_no("Press 'Y' to save or 'N' to skip."):
        dna_filename = choose_filename("formatted_dna")

        if dna_filename is not None:
            output_dna_file = save_formatted_sequence(
                formatted_sequence,
                dna_filename,
        )

        if output_dna_file is not None:
            logger.info("File saved as %s", output_dna_file)

    else: 
        logger.info("Formatted DNA file not saved, continuing to RNA transcription.")


    #STEP 4: Ask user if they wish to transcribe DNA sequence to RNA.
    logger.info("Would you like to convert to RNA?")

    if not request_yes_no("Press 'Y' to convert to RNA or 'N' to cancel"):
        return output_dna_file

    formatted_rna_sequence = transcribe_to_rna(formatted_sequence)

    #(Defensive check)
    if formatted_rna_sequence is None:
        return output_dna_file

    logger.info("formatted RNA sequence: \n%s", formatted_rna_sequence)


    #STEP 5: Ask if user wants to save an RNA file.
    output_rna_file = None

    logger.info("Would you like to save the formatted RNA sequence?")

    if request_yes_no("Press 'Y' to save file or 'N' to skip"):
        rna_filename = choose_filename("formatted_rna")

        if rna_filename is not None: 
            output_rna_file = save_formatted_sequence(
                formatted_rna_sequence,
                rna_filename,
        )

        if output_rna_file is not None:
            logger.info("File saved as %s", output_rna_file)


    #STEP 6: Ask user if wants to translate RNA to Protein.
    logger.info("Would you like to translate the RNA sequence into Protein (unformatted)?")

    if not request_yes_no("Press 'Y' to translate RNA or 'N' to cancel"):
        return output_rna_file or output_dna_file

    amino_acid_sequence = translate_rna(formatted_rna_sequence)

    if amino_acid_sequence is None: 
        return output_rna_file or output_dna_file

    logger.info("Amino acid sequence: \n%s", amino_acid_sequence)
        

    #STEP 7: Ask user if they wish to save the protein sequence file.
    logger.info("Would you like to save the protein sequence?")

    if not request_yes_no("Press 'Y' to save file or 'N' to skip"):
        return output_rna_file or output_dna_file
        
    protein_filename = choose_filename("protein_sequence")

    if protein_filename is None:
        return output_rna_file or output_dna_file

    output_protein_file = save_formatted_sequence(
        amino_acid_sequence,
        protein_filename,
    )

    if output_protein_file is None:
        return output_rna_file or output_dna_file

    return output_protein_file

if __name__ == "__main__":
    setup_logging()
    main()
