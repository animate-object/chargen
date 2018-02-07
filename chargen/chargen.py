#! /usr/bin/env python3

from constants import (
    CLASSES, RACES, BACKGROUNDS, SUBCLASSES_BY_CLASS, ALIGNMENTS
)
from random import choice, seed, randint
from json import dumps

from background_details import generate_random_details, generate_details_for_background

STAT_METHOD = ['3d6']
ABILITIES = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']

def generate_character(random_assign_stats=False, random_details=False, align=False):
    """ Generate data for a DnD character
    """
    class_ = choice(CLASSES)
    subclass = choice(SUBCLASSES_BY_CLASS[class_])
    race = choice(RACES)
    background = choice(BACKGROUNDS)
    alignment = choice(ALIGNMENTS)

    background_details =  (generate_random_details() if random_details 
        else generate_details_for_background(background, alignment if align else None))

    # stats
    stats = roll_stats('3d6')
    if random_assign_stats:
        stats = assign_stats(stats)

    return {
        'alignment': list(alignment),
        'class': class_.capitalize(),
        'subclass': subclass,
        'race': race.capitalize(),
        'background': background.capitalize(),
        'background_details': background_details,
        'stats': stats
    }

def roll_stats(strategy):
    """ Roll level 1 base stats (does not apply racial bonuses)
    """
    if not strategy == '3d6':
        raise NotImplemented("Strategy {} not implemented".format(strategy))
    return [sum([randint(1,6) for _ in range(3)]) for _ in range(6)]

def assign_stats(stats):
    return dict(zip(ABILITIES, stats))

def print_character(char_data):
    pass

if __name__ == '__main__':
    seed()
    char_data = generate_character(True, False, True)
    print(dumps(char_data))
