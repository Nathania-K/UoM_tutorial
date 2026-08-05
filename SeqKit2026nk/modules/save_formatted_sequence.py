import logging
from pathlib import Path

logger = logging.getLogger(__name__)

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