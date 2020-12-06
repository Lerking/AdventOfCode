test_data = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

wd = '/home/jan/projects/AdventOfCode/2020'

customs = []

with open(wd+'/customs.txt', 'r') as ER:
    temp = ""
    for item in ER:
        if item == '\n':
            customs.append(temp)
            temp = ""
            continue
        temp += item.strip('\n')
    customs.append(temp)

def yes_count():
    yesses = []
    summize = 0
    for c in customs:
        yesses.append(set(c))
        summize += len(set(c))
    return summize

print(f'Part 1: {yes_count()}')