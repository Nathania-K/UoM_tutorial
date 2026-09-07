import logging

logger = logging.getLogger(__name__)

#Tranlsates RNA into Protein sequences 
def translate_rna(formatted_rna_sequence):

    #Index of the RNA codons and their translated proteins.
    translation_index = {
        "uuu": "F",
        "uuc": "F",
        "uua": "L",
        "uug": "L",
        "ucu": "S",
        "ucc": "S",
        "uca": "S",
        "ucg": "S",
        "uau": "Y",
        "uac": "Y",
        "ugu": "C",
        "ugc": "C",
        "ugg": "W",
        "cuu": "L",
        "cuc": "L",
        "cua": "L",
        "cug": "L",
        "ccu": "P",
        "ccc": "P",
        "cca": "P",
        "ccg": "P",
        "cau": "H",
        "cac": "H",
        "caa": "Q",
        "cag": "Q",
        "cgu": "R",
        "cgc": "R",
        "cga": "R",
        "cgg": "R",
        "auu": "I",
        "auc": "I",
        "aua": "I",
        "acu": "T",
        "acc": "T",
        "aca": "T",
        "acg": "T",
        "aau": "N",
        "aac": "N",
        "aaa": "K",
        "aag": "K",
        "agu": "S",
        "agc": "S",
        "aga": "R",
        "agg": "R",
        "guu": "V",
        "guc": "V",
        "gua": "V",
        "gug": "V",
        "gcu": "A",
        "gcc": "A",
        "gca": "A",
        "gcg": "A",
        "gau": "D",
        "gac": "D",
        "gaa": "E",
        "gag": "E",
        "ggu": "G",
        "ggc": "G",
        "gga": "G",
        "ggg": "G",
        "aug": "M",
        "uaa": "*",
        "uga": "*",
        "uag": "*"
    }

    # if empty string, returns none and provides warning.
    if not formatted_rna_sequence:
        logger.warning("Cannot translate empty RNA sequence")
        return None

    #cleans the rna sequence and returns a lower case string with joined whitespaces, only accepting 'aucgnx' and calculates untranslated bases.
    rna_sequence = "".join(
        character
        for character in formatted_rna_sequence.lower()
        if character in "aucgnx"
    ) 
    incomplete_bases = len(rna_sequence) % 3

    if incomplete_bases:

        logger.warning("ignoring %d incomplete bases(s) at end of RNA sequence",
        incomplete_bases,
        )

    #Creates empty list of amino acid sequences to be added to after the following loop.
    amino_acids = []

    #Opens loop going through cleaned rna seuqnce, starting at 0, throughout the length of the rna sequence, 3 bases at a time.
    for position in range (0, len(rna_sequence) - incomplete_bases, 3,):
        codon = rna_sequence[position:position + 3] #determines what a codon is (every 3 bases).
        amino_acid = translation_index.get(codon, "X") #converts codon to amino acid. if not found, returns 'X'.
        amino_acids.append(amino_acid) #adds each translated amino acid to list.
    amino_acid_sequence = "".join(amino_acids) #joins all translated amino acids into a seuqnece in a string. 

    logger.info(
        "Translated %d bases into %d amino acids.",
        len(rna_sequence) - incomplete_bases,
        len(amino_acid_sequence),
    )

    return amino_acid_sequence