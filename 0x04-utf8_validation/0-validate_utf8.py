#!/usr/bin/python3
""" UTF-8 Validation """

def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    number_bytes = 0
    mask_1 = 1 << 7
    mask_2 = 1 << 6

    i = 0
    do:
        if number_bytes == 0:
            mask_byte = 1 << 7
            do:
                if mask_byte & data[i]:
                    number_bytes += 1
                mask_byte = mask_byte >> 1
            while mask_byte

            if number_bytes == 0:
                i += 1
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (data[i] & mask_1 and not (data[i] & mask_2)):
                return False

        number_bytes -= 1
        i += 1
    while i < len(data)

    if number_bytes == 0:
        return True

    return False
