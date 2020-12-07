wd = '/home/jan/projects/AdventOfCode/2015'

x = 0
y = 0
houses = [] 
houses.append([x, y, 1])

def next_house(dir):
    global x, y
    global houses
    temp = []
    index = 0
    if dir == '<':
        x -= 1
    if dir == '>':
        x += 1
    if dir == 'v':
        y -= 1
    if dir == '^':
        y += 1
    for ch in houses:
        if ch[0] == x and ch[1] == y:
            houses[index][2] += 1
            return
        index += 1
    temp.append(x)
    temp.append(y)
    temp.append(1)
    houses.append(temp)

with open(wd+"/day_3_input.txt", 'r') as F:
    for l in F:
        for d in l:
            next_house(d)
cnt = [p[2] for p in houses if p[2] >= 1]

print(f'Part 1: {len(cnt)}')
    
print(f'Part 1 alternative: {len(houses)}')