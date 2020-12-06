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

customs_test = []

with open(wd+'/customs.txt', 'r') as ER:
    temp = []
    for item in ER:
        if item == '\n':
            customs_test.append(temp)
            temp = []
            continue
        temp.append(item.strip('\n'))
    customs_test.append(temp)

def yes_all(dat):
    summarize = 0
    for y in dat:
        if len(y) == 1:
            summarize += len(y[0])
            continue
        for a in min(y, key=len):
            cnt = 0
            for c in y:
                cnt += c.count(str(a))
            if cnt/len(y) == 1:
                summarize += 1
    return summarize

print(f'Part 2: {yes_all(customs_test)}')

