from sympy.ntheory.modular import solve_congruence

test_data = ['939', 
            ['7', '13', 'x', 'x', '59', 'x', '31', '19']]

timestamp = int(test_data[0])
shuttles_test = []
for s in test_data[1]:
    if s == 'x':
        continue
    else:
        shuttles_test.append(int(s))

print(f'Timestamp: {timestamp}')
print(f'Shuttles: {shuttles_test}')

def departure(ts, ss):
    dep = []
    for d in range(ts, ts+10):
        tmp = []
        for s in ss:
            if d % s == 0:
                tmp.append(d)
                tmp.append(s)
        if not tmp:
            continue
        else:
            dep.append(tmp)
    return dep

part_1_test = departure(timestamp, shuttles_test)
print(f'Departures: {part_1_test}')
print(f'Part 1 test: {(part_1_test[0][0]-timestamp)*part_1_test[0][1]}')

timestamp = 0
shuttles = []
index = 0
with open('shuttle.txt', 'r') as SD:
    for s in SD:
        if index == 0:
            timestamp = int(s)
            index += 1
            continue
        if index == 1:
            for ss in s.split(','):
                if ss == 'x':
                    continue
                else:
                    shuttles.append(int(ss))

print(f'Timestamp: {timestamp}')
print(f'Shuttles: {shuttles}')

part_1 = departure(timestamp, shuttles)
print(f'Departures: {part_1}')
print(f'Part 1: {(part_1[0][0]-timestamp)*part_1[0][1]}')

def timestamps(ss, st):
    t = st
    found = False
    while found == False:
        for si, s in enumerate(ss):
            if s == 'x':
                continue
            elif (t+si) % int(s) != 0:
                t += int(ss[0])
                break
            elif (t+si) % int(s) == 0:
                if si == len(ss)-1:
                    found = True
                continue
    return t

shuttles_test = []
for s in test_data[1]:
    shuttles_test.append(s)

shuttles = []
index = 0
with open('shuttle.txt', 'r') as SD:
    for s in SD:
        if index == 0:
            timestamp = int(s)
            index += 1
            continue
        if index == 1:
            for ss in s.split(','):
                shuttles.append(ss)

print(f'Part 2 test: {timestamps(shuttles_test, 7)-len(shuttles_test)}')
#print(f'Part 2: {timestamps(shuttles, 100000000000009)-len(shuttles)}')

with open('shuttle.txt') as f:
    shuttles = [line.strip() for line in f.readlines()]
bus_times = [(-i, int(x)) for i, x in enumerate(shuttles[1].split(',')) if x != 'x']
print(f'Part 2: {solve_congruence(*bus_times)[0]}')