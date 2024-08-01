#!/usr/bin/python3
"""Solves the lock boxes puzzle"""


def find_next_opened_box(opened_boxes):
    """Finds the next opened box
    Args:
        opened_boxes (dict): Dictionary containing already opened boxes
    Returns:
        list: List of keys contained in the opened box
    """
    for index, box in opened_boxes.items():
        if box['status'] == 'opened':
            box['status'] = 'opened/checked'
            return box['keys']
    return None


def can_unlock_all(boxes):
    """Checks if all boxes can be opened
    Args:
        boxes (list): List containing all boxes with keys
    Returns:
        bool: True if all boxes can be opened, False otherwise
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    opened_boxes = {}
    while True:
        if not opened_boxes:
            opened_boxes[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = find_next_opened_box(opened_boxes)
        if keys:
            for key in keys:
                try:
                    if opened_boxes.get(key) and opened_boxes[key]['status'] == 'opened/checked':
                        continue
                    opened_boxes[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif any(box['status'] == 'opened' for box in opened_boxes.values()):
            continue
        elif len(opened_boxes) == len(boxes):
            break
        else:
            return False

    return len(opened_boxes) == len(boxes)


def main():
    """Entry point"""
    can_unlock_all([[]])


if __name__ == '__main__':
    main()
