test_data = ['939', 
            ['7', '13', 'x', 'x', '59', 'x', '31', '19']]

timestamp = int(test_data[0])
shuttles = []
for s in test_data[1]:
    if s == 'x':
        continue
    else:
        shuttles.append(int(s))

print(f'Timestamp: {timestamp}')
print(f'Shuttles: {shuttles}')

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

part_1_test = departure(timestamp, shuttles)
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