from constants import BACKGROUND_DATA
from random import choice, shuffle

IDEAL, TRAIT, BOND, FLAW = 'ideal', 'trait', 'bond', 'flaw'
BASE_DEETS = [IDEAL, TRAIT, BOND, FLAW]

def generate_details_for_background(background, alignment=None):
    """ Generate appropriate details for a background. Selects based on alignment if provided.
    """
    deets = {}
    source = BACKGROUND_DATA[background]
    for attr in source:
        if attr == IDEAL:
            val = ideal_from_alignment(source[attr], alignment) if alignment else random_ideal(source[attr])
            if not val:
                raise AttributeError("Unable to find ideal for alignment {} for background {}.".format(alignment, background))
        else:
            val = choice(source[attr])
        deets[attr] = val
    return deets
    

def generate_random_details():
    """ Generate background details from a random selection of backgrounds
    """
    deets = {}
    for attr in BASE_DEETS:
        source = BACKGROUND_DATA[choice(list(BACKGROUND_DATA))]
        deets[attr] = random_ideal(source[attr]) if attr == IDEAL else choice(source[attr])
    return deets

def random_ideal(ideals):
    return choice([ideal for alignment_list in ideals.values() for ideal in alignment_list])

def ideal_from_alignment(ideals, alignment):
    """ Get one of the ideals matching the provided alignment tuple
    Alignment is assumed to be a 2-ple of form (<lawful - chaotic>, <good - evil>)
    """
    applicable_alignment = ['any'] + list(alignment)
    shuffle(applicable_alignment)
    for val in applicable_alignment:
        try:
            return choice(ideals[val])
        except KeyError:
            continue

