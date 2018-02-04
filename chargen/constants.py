#i -------------------------------------------------------- #
#   class constants
# ------------------
#   there are 12 character classes, all specified in the DMG
# -------------------------------------------------------- #

BARBARIAN = 'barbarian'
BARD = 'bard'
CLERIC = 'cleric'
DRUID = 'druid'
FIGHTER = 'fighter'
MONK = 'monk'
PALADIN = 'paladin'
RANGER = 'ranger'
ROGUE = 'rogue'
SORCERER = 'sorcerer'
WARLOCK = 'warlock'
WIZARD = 'wizard'

# --------------------------------------------------------- #
#   race constants
# -----------------
#   base game races are defined in the PHB
#   supplemental races are specified in volos
#   which categorizes monstrous races separately
#   there are apparently also wizards definitions
#   for Aarakocra and Genasi from the elemental evil books  
# --------------------------------------------------------- #

AARAKOCRA = 'aarakocra'
AASIMAR = 'aasimar'
BUGBEAR = 'bugbear'
DWARF = 'dwarf'
DRAGONBORN = 'dragonborn'
ELF = 'elf'
FIRBOLGS = 'firbolgs'
HALFLING = 'halfling'
HALF_ELF = 'half-elf'
HALF_ORC = 'half-orc'
HUMAN = 'human'
GENASI = 'genasi'
GNOME = 'gnome'
GOBLIN = 'goblin'
GOLIATH = 'goliath'
HOBGOBLIN = 'hobgoblin'
KENKU = 'kenku'
KOBOLD = 'kobold'
LIZARDFOLK = 'lizardfolk'
ORC = 'orc'
TABAXI = 'tabaxi'
TRITON = 'triton'
TIEFLING = 'tiefling'
YUAN_TI_PUREBLOOD = 'yuan-ti pureblood'

# -------------------------------------------------------- #
#   background constants
# -----------------------
#   these are the 13 backgrounds from the DMG
# -------------------------------------------------------- #

ACOLYTE = 'acolyte'
CHARLATAN = 'charlatan'
CRIMINAL = 'criminal'
ENTERTAINER = 'entertainer'
FOLK_HERO = 'folk hero'
GUILD_ARTISAN = 'guild artisan'
HERMIT = 'hermit'
NOBLE = 'noble'
OUTLANDER = 'outlander'
SAGE = 'sage'
SAILOR = 'sailor'
SOLDIER = 'soldier'
URCHIN = 'urchin'

# -------------------------------------------------------- #
#   collections
# -------------------------------------------------------- #

CLASSES = [
    BARBARIAN, BARD, CLERIC, DRUID, FIGHTER, MONK,
    PALADIN, RANGER, ROGUE, SORCERER, WARLOCK, WIZARD
]

BASE_RACES = [DWARF, ELF, HUMAN, HALFLING]
EXOTIC_RACES = [DRAGONBORN, GNOME, HALF_ELF, HALF_ORC, TIEFLING]
VOLOS_RACES = [AASIMAR, FIRBOLGS, GOLIATH, KENKU, LIZARDFOLK, TABAXI, TRITON]
VOLOS_MONSTER_RACES = [BUGBEAR, GOBLIN, HOBGOBLIN, ORC, YUAN_TI_PUREBLOOD]
ELEMENTAL_EVIL_RACES = [AARAKOCRA, GENASI]

RACES = BASE_RACES + EXOTIC_RACES + \
        VOLOS_RACES + VOLOS_MONSTER_RACES + \
        ELEMENTAL_EVIL_RACES

BACKGROUNDS = [
    ACOLYTE, CHARLATAN, CRIMINAL, ENTERTAINER, FOLK_HERO, GUILD_ARTISAN,
    HERMIT, NOBLE, OUTLANDER, SAGE, SAILOR, SOLDIER, URCHIN
]


# -------------------------------------------------------- #
#   mappings
# -------------------------------------------------------- #

CORE_SUBCLASSES_BY_CLASS = {
    BARBARIAN: [
        'Path of the Berserker',
        'Path of the Totem Warrior'
    ],
    BARD: [
        'College of Lore',
        'College of Valor'
    ],
    CLERIC: [
        'Knowledge Domain',
        'Life Domain',
        'Light Domain',
        'Nature Domain',
        'Tempest Domain',
        'Trickery Domain',
        'War Domain',
        'Death Domain'  # from DMG, which is 'core'
    ],
    DRUID: [
        'Circle of the Land',
        'Circle of the Moon'
    ],
    FIGHTER: [
        'Champion',
        'Battle Master',
        'Eldritch Knight'
    ],
    MONK: [
        'Way of the Open Hand',
        'Way of Shadow',
        'Way of the Four Elements'
    ],
    PALADIN: [
        'Oath of Devotion',
        'Oath of the Ancients',
        'Oath of Vengeance'
    ],
    RANGER: [
        'Hunter',
        'Beast Master'
    ],
    ROGUE: [
        'Thief',
        'Assassin',
        'Arcane Trickster'
    ],
    SORCERER: [
        'Wild Magic',
        'Draconic Bloodline'
    ],
    WARLOCK: [
        'The Archfey',
        'The Fiend',
        'The Great Old One'
    ],
    WIZARD: [
        'School of Abjuration',
        'School of Conjuration',
        'School of Divination',
        'School of Enchantment',
        'School of Evocation',
        'School of Illusion',
        'School of Necromancy',
        'School of Transmutation'
    ]
}

XAN_SUBCLASSES_BY_CLASS = {
    BARBARIAN: [
        'Path of the Ancestral Guardian',
        'Path of the Storm Herald',
        'Path of the Zealot'
    ],
    BARD: [
        'College of Glamour',
        'College of Swords',
        'College of Whispers'
    ],
    CLERIC: [
        'Forge Domain',
        'Grave Domain'
    ],
    DRUID: [
        'Circle of Dreams',
        'Circle of the Shepherd'
    ],
    FIGHTER: [
        'Arcane Archer',
        'Cavalier',
        'Samurai'
    ],
    MONK: [
        'Way of the Drunken Master',
        'Way of the Kensei',
        'Way of the Sun Soul'
    ],
    PALADIN: [
        'Oath of Conquest',
        'Oath of Redemption'
    ],
    RANGER: [
        'Gloom Stalker',
        'Horizon Walker',
        'Monster Slayer'
    ],
    ROGUE: [
        'Inquisitive',
        'Mastermind',
        'Scout',
        'Swashbuckler',
    ],
    SORCERER: [
        'Divine Soul',
        'Shadow Magic',
        'Storm Sorcery'
    ],
    WARLOCK: [
        'The Celestial',
        'The Hexblade'
    ],
    WIZARD: [
        'War Magic'
    ]
}

SUBCLASSES_BY_CLASS = {
    class_: CORE_SUBCLASSES_BY_CLASS[class_] + XAN_SUBCLASSES_BY_CLASS[class_]
    for class_ in CLASSES
}
