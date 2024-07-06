#!/usr/bin/python3
"""BOXES BOXES"""


def canUnlockAll(boxes):
    """
    take boxes
        create set of keys
            go to box0
                get all keys and add them keyscollected
            start opening boxes from keyscollected
                go to each box of each key
                    and take the keys from it and add them to keyscollected
                keep looping through all setof keys
            ignore keys that dont have box
            track opening of boxes by a counter, if at end it
            equal to lentgh of boxes it mean all boxes unlock
            OPTIMIZE IDEA :
                if we add 0 to setofkeys at start, we dont need for in 23
    """
    num_boxes = len(boxes)
    keys_collected = [0]
    unlocked_boxes = 0
    current_key_index = 0

    while current_key_index < len(keys_collected):
        current_box = keys_collected[current_key_index]
        for key in boxes[current_box]:
            if 0 < key < num_boxes and key not in keys_collected:
                keys_collected.append(key)
                unlocked_boxes += 1
        current_key_index += 1

    return unlocked_boxes == num_boxes - 1
