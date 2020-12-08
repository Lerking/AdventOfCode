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

santa_x = 0
santa_y = 0

def santa_move(dir):
    global santa_x, santa_y
    global houses
    temp = []
    index = 0
    if dir == '<':
        santa_x -= 1
    if dir == '>':
        santa_x += 1
    if dir == 'v':
        santa_y -= 1
    if dir == '^':
        santa_y += 1
    for ch in houses:
        if ch[0] == santa_x and ch[1] == santa_y:
            houses[index][2] += 1
            return
        index += 1
    temp.append(santa_x)
    temp.append(santa_y)
    temp.append(1)
    houses.append(temp)

robo_x = 0
robo_y = 0

def robo_move(dir):
    global robo_x, robo_y
    global houses
    temp = []
    index = 0
    if dir == '<':
        robo_x -= 1
    if dir == '>':
        robo_x += 1
    if dir == 'v':
        robo_y -= 1
    if dir == '^':
        robo_y += 1
    for ch in houses:
        if ch[0] == robo_x and ch[1] == robo_y:
            houses[index][2] += 1
            return
        index += 1
    temp.append(robo_x)
    temp.append(robo_y)
    temp.append(1)
    houses.append(temp)

houses = []
index = 0
with open(wd+"/day_3_input.txt", 'r') as F:
    for l in F:
        for d in l:
            if index % 2 == 0:
                santa_move(d)
            if index % 2 == 1:
                robo_move(d)
            index += 1
            
print(f'Part 2: {len(houses)}')
