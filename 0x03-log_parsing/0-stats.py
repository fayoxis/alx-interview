#!/usr/bin/python3

import sys


def print_msg(status_codes_dict, total_file_size):
    """
    Print the total file size and the count of each status code.

    Args:
        status_codes_dict (dict): Dictionary containing the count of each status code.
        total_file_size (int): Total size of the files.

    Returns:
        None
    """
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_codes_dict.items()):
        if count != 0:
            print(f"{code}: {count}")


def process_logs():
    """
    Process the log lines from stdin and count the status codes and total file size.

    Returns:
        None
    """
    total_file_size = 0
    counter = 0
    status_codes_dict = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }

    try:
        for line in sys.stdin:
            parsed_line = line.strip().split()[::-1]  # Invert and trim the line

            if len(parsed_line) > 2:
                counter += 1

                if counter <= 10:
                    total_file_size += int(parsed_line[0])  # File size
                    status_code = parsed_line[1]  # Status code

                    if status_code in status_codes_dict:
                        status_codes_dict[status_code] += 1

                if counter == 10:
                    print_msg(status_codes_dict, total_file_size)
                    counter = 0

    finally:
        print_msg(status_codes_dict, total_file_size)


if __name__ == "__main__":
    process_logs()
