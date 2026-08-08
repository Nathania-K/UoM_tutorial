import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def save_formatted_sequence(formatted_sequence, filename="formatted_sequence.txt", output_dir=None):
    """ 
    Saves GenBank formatted sequence to output folder in parent directory (UOM_Tutorials).
    If OSError (i.e. due to unexpected format), returns None and no file saved.
    """ 

    #Gets and sets the project directory (UOM_Tutorial) path and attaches 'output' file
    if not formatted_sequence:
        logger.warning("Cannot save an empty formatted sequence.")
        return None

    #if no save path supplied, returns current working directory from where program starts.
    if output_dir is None:
        output_dir = Path.cwd() / "outputs" #attaches "outputs" folder to cwd.
    else:
        output_dir = Path(output_dir) #If output directory supplied, converts to path object. 

    output_file = output_dir / filename #combines output directory and filname for complete path.

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