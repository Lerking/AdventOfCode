from collections import defaultdict

with open('joltage.txt') as f:
    jl = [int(line) for line in f.readlines()]
    jl.append(0)
    jl = sorted(jl)
    jl.append(jl[-1:][0]+3)

ones = 0
threes = 0
for i, n in enumerate(jl):
    if i < 1:
        continue
    prev = jl[i-1:i]
    if n - prev[0] == 1:
        ones += 1
    if n - prev[0] == 3:
        threes += 1

print(f'Part 1: {ones*threes}')

def valid_chain(adapters):
    valids = 0
    valid = True
    while valid == True:
        for i, v in enumerate(adapters):
            tmp = adapters.copy()
            if i == 0:
                continue
            prev = tmp[i-1:i]
            if not 1 <= v-prev[0] <= 3:
                return valids
            tmp.pop(1)
            valids += valid_chain(tmp)
        break
    return valids       

#valids = valid_chain(jl)

paths = defaultdict(int)
paths[0] = 1
for i in range(1, len(jl)):
    for j in range(i)[::-1]:
        if jl[i] - jl[j] > 3:
            break
        paths[i] += paths[j]

print(paths[len(jl)-1])
print(paths)