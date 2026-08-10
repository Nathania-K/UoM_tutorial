import logging

logger = logging.getLogger(__name__)

def translate_rna(formatted_rna_sequence):

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

    if not formatted_rna_sequence:
        logger.warning("Cannot translate empty RNA sequence")
        return None

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

    amino_acids = []

    for position in range (0, len(rna_sequence) - incomplete_bases, 3,):
        codon = rna_sequence[position:position + 3]
        amino_acid = translation_index.get(codon, "X")
        amino_acids.append(amino_acid)
    amino_acid_sequence = "".join(amino_acids)

    logger.info(
        "Translated %d bases into %d amino acids.",
        len(rna_sequence) - incomplete_bases,
        len(amino_acid_sequence),
    )

    return amino_acid_sequence