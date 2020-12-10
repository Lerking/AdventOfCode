wd = '/home/jan/projects/AdventOfCode/2015'

grid = [[0]*1000]*1000

lights = []

with open(wd+"/lights.txt", 'r') as F:
    for l in F:
        tmp = []
        for w in l.strip('\n').split():
            if w in ['turn', 'through']:
                continue
            if w in ['on', 'off', 'toggle']:
                tmp.append(w)
                continue
            rc = []
            for f in w.split(','):
                rc.append(int(f))
            tmp += rc[::-1]
        lights.append(tmp)

def lights_on(start_row, start_col, end_row, end_col):
    global grid
    for row in range(start_row, end_row+1):
        for col in range(start_col, end_col+1):
            grid[row][col] = 1

def lights_off(start_row, start_col, end_row, end_col):
    global grid
    for row in range(start_row, end_row+1):
        for col in range(start_col, end_col+1):
            grid[row][col] = 0

def lights_toggle(start_row, start_col, end_row, end_col):
    global grid
    for row in range(start_row, end_row+1):
        for col in range(start_col, end_col+1):
            if grid[row][col] == 0:
                grid[row][col] = 1
            elif grid[row][col] == 1:
                grid[row][col] = 0

for i in lights:
    if i[0] == 'on':
        lights_on(i[2], i[1], i[4], i[3])
        continue
    if i[0] == 'off':
        lights_off(i[2], i[1], i[4], i[3])
        continue
    if i[0] == 'toggle':
        lights_toggle(i[2], i[1], i[4], i[3])
        continue

x = 0
for l in grid:
    x += l.count(True)
print(f'Part 1 lights on: {x}')