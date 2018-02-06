from random import randint

def roll_on_table(table, roll=None):
    """ Allows rolling on a table like those defined in DnD material
    You can either provide a dice roll or the method will generate one based on the range of the table
    """
    _unpacked_table = {}
    for key in table:
        if '-' in key:
            keys = key.split('-')
            low, high = int(keys[0]), int(keys[1]) if not key == '00' else 100
            for val in range(low, high + 1):
                _unpacked_table[val] = table[key]
        else:
            key = int(key) if not key == '00' else 100
            _upacked_table[key] = table[key]

    if not roll:
        roll = randint(1, len(_unpacked_table))

    return _unpacked_table[roll]

def roll_from_str(roll_str):
    """ roll dice in form ndm+k
    Where n is the number of dice, m is the cardinality of the dice, and k is a constant modifier
    """
    print(roll_str)
    roll_str = roll_str.lower()
    d_idx = roll_str.find('d')
    n = roll_str[:d_idx]

    second_part = roll_str[(d_idx + 1):]
    m, k = second_part, 0
    plus_idx = second_part.find('+')

    if plus_idx > 0: 
        m = second_part[:plus_idx]
        k = second_part[(plus_idx + 1):]

    total = 0

    for sub_roll in range(int(n)):
        total += randint(1,int(m))
    print(n, m, k)
    return total + int(k)

if __name__ == '__main__':
    print(roll_from_str('4d8'))
    print(roll_from_str('1d100'))
    print(roll_from_str('3d6'))
    print(roll_from_str('4d8+6'))
