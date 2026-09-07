import logging 

logger = logging.getLogger(__name__)

def transcribe_to_rna(formatted_sequence): 
    """
    Converts formatted DNA sequence and converts into rna string.
    """

    if not formatted_sequence:
        return None

    #index to convert all 't's to 'u'
    transcription_index = str.maketrans({
        "t": "u",
        "T": "u",
    })

    #Takes inputted dna string and converts all 't's to 'u' using the index above and enters to lower case. 
    return formatted_sequence.translate(transcription_index).lower()