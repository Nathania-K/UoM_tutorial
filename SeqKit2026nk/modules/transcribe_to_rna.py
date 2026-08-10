import logging 

logger = logging.getLogger(__name__)

def transcribe_to_rna(formatted_sequence): 
    """
    Converts formatted DNA sequence and converts into rna string.
    """

    if not formatted_sequence:
        return None

    transcription_index = str.maketrans({
        "a": "u",
        "t": "a",
        "c": "g",
        "g": "c",
        "A": "u",
        "T": "a",
        "C": "g",
        "G": "c",
    })

    return formatted_sequence.translate(transcription_index)