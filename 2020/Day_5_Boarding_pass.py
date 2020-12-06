import math

test_data = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

wd = '/home/jan/projects/AdventOfCode/2020'

boarding_passes = []

with open(wd+'/boarding_pass.txt', 'r') as ER:
    for item in ER:
        boarding_passes.append(item.strip('\n'))

def read_boarding_pass(bp):
    temp = []
    lower_row = 0
    upper_row = 127
    lower_seat = 0
    upper_seat = 7
    temp.append(bp)
    for r in bp:
        if r == 'F':
            upper_row = math.floor((upper_row-lower_row)/2)+lower_row
            continue
        if r == 'B':
            lower_row = math.floor((upper_row-lower_row)/2)+lower_row
            continue
        if r == 'L':
            upper_seat = math.floor((upper_seat-lower_seat)/2)+lower_seat
            continue
        if r == 'R':
            lower_seat = math.floor((upper_seat-lower_seat)/2)+lower_seat
            continue

    temp.append(upper_row)
    temp.append(upper_seat)
    temp.append(upper_row*8+upper_seat)

    return temp

test_result = []
for bp in test_data:
    test_result.append(read_boarding_pass(bp))

print(test_result)

result = []
for bp in boarding_passes:
    result.append(read_boarding_pass(bp))

print(f'Part 1: {max([id[3] for id in result])}')

data = sorted([id[3] for id in result])

index = 0
for x in data:
    if index == 0:
        index += 1
        continue
    if data[index-1] == x-2:
        print(f'Part 2: {x-1}')
    index += 1
