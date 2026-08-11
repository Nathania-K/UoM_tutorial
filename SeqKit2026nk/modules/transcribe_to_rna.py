import logging 

logger = logging.getLogger(__name__)

def transcribe_to_rna(formatted_sequence): 
    """
    Converts formatted DNA sequence and converts into rna string.
    """

    if not formatted_sequence:
        return None

    transcription_index = str.maketrans({
        "t": "u",
        "T": "u",
    })

    return formatted_sequence.translate(transcription_index).lower()