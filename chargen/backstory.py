from chargen.constants import HALF_ORC, HALF_ELF, TIEFLING, ELF, ORC, HUMAN, ALIGNMENTS
from random import choice, randint, shuffle

DEVIL = 'devil'

def generate_mixed_race_parents(race, mother_father):
    roll = randint(1, 8)
    if race == HALF_ELF:
        if roll <= 5:
            parent_races = [ELF, HUMAN]
        elif roll == 6:
            parent_races = [ELF, HALF_ELF]
        elif roll == 7:
            parent_races = [HUMAN, HALF_ELF]
        else:
            parent_races = [HALF_ELF, HALF_ELF]
    elif race == HALF_ORC:
        if roll <= 3:
            parent_races = [ORC, HUMAN]
        elif roll <= 5:
            parent_races = [ORC, HALF_ORC]
        elif roll <= 7:
            parent_races = [HUMAN, HALF_ORC]
        else:
            parent_races = [HALF_ORC, HALF_ORC]
    elif race == TIEFLING:
        if roll <= 4:
            parent_races = [HUMAN, HUMAN]
        elif roll <= 6:
            parent_races = [TIEFLING, HUMAN]
        elif roll == 7:
            parent_races = [TIEFLING, DEVIL]
        else:
            parent_races = [HUMAN, DEVIL]

    return list(zip(mother_father, parent_races))
 

def generate_parentage(race, extra=True):
    mother_father = ['Mother', 'Father']
    shuffle(mother_father)
    roll = randint(1, 100)
    if roll <= 5:
        return list(zip(mother_father, ['unknown', 'unknown']))

    if race in [HALF_ORC, HALF_ELF, TIEFLING]:
        parents = generate_mixed_race_parents(race, mother_father)
    else:
        parents = list(zip(mother_father, [race, race]))
    
    return parents



def generate_backstory(race):
    parents = generate_parentage(race)

    return {
        'parents': parents
    }

