import logging 

logger = logging.getLogger(__name__)

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

