layers = []
evaluate = []

with open('/storage/emulated/0/documents/adventorcode/2019/day_8_input.txt', 'r') as F:
    pixels = []
    rows = []
    pixel_index = 0
    row_index = 0
    for x in F:
        for l in x.strip('\n'):
            pixels.append(int(l))
            pixel_index += 1
            if pixel_index == 25:
                rows.append(pixels)
                pixels = []
                pixel_index = 0
                row_index += 1
            elif row_index == 6:
                layers.append(rows)
                rows = []
                row_index =+ 1
            else:
                continue

print(layers)

ev = []
zeros = 0
ones = 0
twos = 0
for l in layers:
    for r in l:
        for p in r:
            if p == 0:
                zeros += 1
            elif p == 1:
                ones += 1
            elif p == 2:
                twos += 1
            else:
                continue
    ev.append(zeros)
    ev.append(ones)
    ev.append(twos)
    zeros = 0
    ones = 0
    twos = 0
    evaluate.append(ev)
    ev = []

print(evaluate)

fewest_zeros = min(evaluate, key=lambda x: x[0])
print(fewest_zeros)
print(fewest_zeros[1]*fewest_zeros[2])
    
