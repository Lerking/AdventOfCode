wd = '/home/jan/projects/AdventOfCode/2015'

grid = [[False]*1000]*1000

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
            grid[row][col] = True

def lights_off(start_row, start_col, end_row, end_col):
    global grid
    for row in range(start_row, end_row+1):
        for col in range(start_col, end_col+1):
            grid[row][col] = False

def lights_toggle(start_row, start_col, end_row, end_col):
    global grid
    for row in range(start_row, end_row+1):
        for col in range(start_col, end_col+1):
            v = grid[row][col]
            grid[row][col] = not(v)

for i in lights:
    if i[0] == 'on':
        lights_on(i[1], i[2], i[3], i[4])
        continue
    if i[0] == 'off':
        lights_off(i[1], i[2], i[3], i[4])
        continue
    if i[0] == 'toggle':
        lights_toggle(i[1], i[2], i[3], i[4])
        continue

print(f'Part 1 lights on: {sum(x.count(True) for x in grid)}')