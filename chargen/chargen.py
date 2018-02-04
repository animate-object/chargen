#! /usr/bin/env python3

from constants import CLASSES, RACES, BACKGROUNDS
from random import choice, seed
from json import dumps

def generate_character():
    """ Generate data for a DnD character
    """
    class_ = choice(CLASSES)
    race = choice(RACES)
    background = choice(BACKGROUNDS)

    return {
        'class': class_,
        'race': race,
        'background': background
    }




def print_character(char_data):
    pass

if __name__ == '__main__':
    seed()
    char_data = generate_character()
    print(dumps(char_data))
