def calc(g):
    return 2*g[0]*g[1]+2*g[1]*g[2]+2*g[0]*g[2]+g[0]*g[1]

def rib(g):
    return 2*g[0]+2*g[1]+g[0]*g[1]*g[2]
    
GIFTS = []
wrapping = 0
ribbon = 0

with open("day_2_input.txt", 'r') as F:
    temp = []
    for line in F:
        for v in line.split("x"):
            temp.append(int(v))
        temp.sort()
        GIFTS.append(temp)
        temp = []

print(GIFTS)

for v in GIFTS:
    wrapping += calc(v)
    ribbon += rib(v)

print(wrapping)    #day 2, part 1
print(ribbon)      #day 2, part 2
