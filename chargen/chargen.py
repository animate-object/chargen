#! /usr/bin/env python3

from argparse import ArgumentParser

from constants import (
    CLASSES, RACES, BACKGROUNDS, SUBCLASSES_BY_CLASS, ALIGNMENTS, SEXES
)
from random import choice, seed, randint
from json import dumps

from background_details import generate_random_details, generate_details_for_background

STAT_METHOD = ['3d6']
ABILITIES = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']

def generate_character(
    random_assign_stats=False, random_details=False, align=False,
    **kwargs
):
    """ Generate data for a DnD character
    """
    class_ = choice(CLASSES) if not kwargs.get('class_') else kwargs['class_']
    subclass = choice(SUBCLASSES_BY_CLASS[class_])
    race = choice(RACES) if not kwargs.get('race') else kwargs['race']
    background = choice(BACKGROUNDS) if not kwargs.get('background') else kwargs['background']
    sex = choice(SEXES) if not kwargs.get('sex') else kwargs['sex']

    alignment = choice(ALIGNMENTS)


    background_details =  (generate_random_details() if random_details 
        else generate_details_for_background(background, alignment if align else None))

    # stats
    stats = roll_stats('3d6')
    if random_assign_stats:
        stats = assign_stats(stats)

    return {
        'sex': sex,
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
    
    parser = ArgumentParser(description='cli to randomly generate dnd characters')
    parser.add_argument('-r', '--race', action='store', default=None, choices=RACES)
    parser.add_argument('-c', '--class', action='store', default=None, choices=CLASSES)
    parser.add_argument('-b', '--background', action='store', default=None, choices=BACKGROUNDS)
    parser.add_argument('-s', '--sex', action='store', default=None, choices=SEXES)

    parser.add_argument('-a', '--align', action='store_true')
    parser.add_argument('-t', '--stat-assign', action='store_true')
    parser.add_argument('-d', '--random-details', action='store_true')

    args = parser.parse_args()

    chargen_kwargs = dict(
        race=args.race,
        class_=getattr(args, 'class', None),
        background=args.background,
        sex=args.sex
    )
    
    char_data = generate_character(
            args.stat_assign, args.random_details, args.align, **chargen_kwargs
    )
    print(dumps(char_data))
