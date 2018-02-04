#! /usr/bin/env python3

from constants import CLASSES, RACES, BACKGROUNDS, SUBCLASSES_BY_CLASS
from random import choice, seed, randint
from json import dumps

STAT_METHOD = ['3d6']
ABILITIES = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']

def generate_character(random_assign_stats=False):
    """ Generate data for a DnD character
    """
    class_ = choice(CLASSES)
    subclass = choice(SUBCLASSES_BY_CLASS[class_])
    race = choice(RACES)
    background = choice(BACKGROUNDS)

    # stats
    stats = roll_stats('3d6')
    if random_assign_stats:
        stats = assign_stats(stats)

    return {
        'class': class_.capitalize(),
        'subclass': subclass,
        'race': race.capitalize(),
        'background': background.capitalize(),
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
    char_data = generate_character(random_assign_stats=True)
    print(dumps(char_data))
