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
    pass

