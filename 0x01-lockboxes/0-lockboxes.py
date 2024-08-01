#!/usr/bin/python3
"""Solves the lock boxes puzzle"""

def get_next_opened_box(opened_boxes):
    """
    Finds the next opened box and marks it as checked.

    Args:
        opened_boxes (dict): Dictionary of opened boxes and their keys

    Returns:
        list: Keys contained in the next opened box, or None if no more opened boxes
    """
    for box_index, box in opened_boxes.items():
        if box['status'] == 'opened':
            box['status'] = 'opened/checked'
            return box['keys']
    return None

def can_unlock_all(boxes):
    """
    Checks if all boxes can be opened.

    Args:
        boxes (list): List of boxes and their keys

    Returns:
        bool: True if all boxes can be opened, False otherwise
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    opened_boxes = {}
    opened_boxes[0] = {'status': 'opened', 'keys': boxes[0]}

    while True:
        keys = get_next_opened_box(opened_boxes)
        if keys:
            for key in keys:
                try:
                    if opened_boxes.get(key) and opened_boxes[key]['status'] == 'opened/checked':
                        continue
                    opened_boxes[key] = {'status': 'opened', 'keys': boxes[key]}
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box['status'] for box in opened_boxes.values()]:
            continue
        elif len(opened_boxes) == len(boxes):
            break
        else:
            return False

    return len(opened_boxes) == len(boxes)

def main():
    """Entry point"""
    print(can_unlock_all([[]])) # True

if __name__ == '__main__':
    main()
