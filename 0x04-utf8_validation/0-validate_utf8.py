#!/usr/bin/python3
""" UTF-8 Validation Utility """


def validUTF8(data):
    """
    Checks if given list of integers represents valid UTF-8 encoded string.
    
    Args:
        data (list): A list of integers representing bytes.
        
    Returns:
        bool: True if input data valid UTF-8 encoded string, False otherwise.
    """
    num_bytes = 0
    mask_1 = 1 << 7
    mask_2 = 1 << 6
    i = 0

    while i < len(data):
        mask_byte = 1 << 7

        # Determine the number of bytes in the current UTF-8 character
        if num_bytes == 0:
            while mask_byte & data[i]:
                num_bytes += 1
                mask_byte = mask_byte >> 1

            # Skip ASCII characters
            if num_bytes == 0:
                i += 1
                continue

            # Invalid cases according to the UTF-8 definition
            if num_bytes == 1 or num_bytes > 4:
                return False

        # Validate the remaining bytes in the current UTF-8 character
        else:
            # Check if the current byte has the correct format
            if not (data[i] & mask_1 and not (data[i] & mask_2)):
                return False

        num_bytes -= 1
        i += 1

    # All bytes were processed successfully
    if num_bytes == 0:
        return True

    # Invalid UTF-8 sequence
    return False
