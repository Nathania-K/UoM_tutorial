import logging 
from SeqKit2026nk.utils.util_mods import request_integer

logger = logging.getLogger(__name__)

def request_format_settings(
    default_block_size=10,
    default_blocks_per_line=6,
):
    """
    Collects user formatting settings and returns tuple with both values or None if cancelled.
    Cancelling will return None.
    Uses request_block_line_integer() function in util.mod for 
    """

    block_size = request_integer(
        "block size",
        default_block_size,
    )

    if block_size is None:
        return None

    blocks_per_line = request_integer(
        "blocks per line",
        default_blocks_per_line,
    )

    if blocks_per_line is None:
        return None 

    return block_size, blocks_per_line
