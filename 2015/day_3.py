import math
    
DIRECT = []

with open("/storage/emulated/0/documents/adventorcode/2015/day_3_input.txt", 'r') as F:
    for l in F:
        for d in l:
            DIRECT.append(d)

print(DIRECT)
print(len(DIRECT))

GRID = []
index = 0
temp = []
for y in range(int(math.sqrt(len(DIRECT)))):
    for x in range(int(math.sqrt(len(DIRECT)))):
        temp.append(index)
        index += 1
    GRID.append(temp)
    temp = []
    
print(GRID)

VISITS = {}
pos_x = int(math.sqrt(len(DIRECT))/2)
pos_y = pos_x
print(pos_x, pos_y)