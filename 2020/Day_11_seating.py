import copy

with open('seats_test.txt', 'r') as S:
    rows_test = [l.strip() for l in S.readlines()]

seats_test = []
for r in rows_test:
    lst = []
    lst[:0]=r
    seats_test.append(lst)

with open('seats.txt', 'r') as S:
    rows = [l.strip() for l in S.readlines()]

seats = []
for r in rows:
    lst = []
    lst[:0]=r
    seats.append(lst)

seat_arrangement = []

def seat_arr(sa):
    global seat_arrangement
    seata = []
    for ri, r in enumerate(sa):
        row_arr = []
        for si, s in enumerate(r):
            if ri == 0 and si > 0:
                sr = 0
                ss = -1
            elif ri == 0 and si == 0:
                sr = 0
                ss = 0
            elif ri > 0 and si == 0:
                sr = -1
                ss = 0
            elif ri > 0 and si > 0:
                sr = -1
                ss = -1
            if s == '.':
                row_arr.append(s)
                continue
            if s == '#':
                occ = 0
                for cri in range(sr, 2):
                    if cri+ri > len(sa)-1:
                        continue
                    for csi in range(ss, 2):
                        if cri == 0 and csi == 0:
                            continue
                        if si+csi > len(r)-1:
                            continue
                        if sa[ri+cri][si+csi] == '#':
                            occ += 1
                if occ >= 4:
                    row_arr.append('L')
                else:
                    row_arr.append(s)
                continue
            if s == 'L':
                occ = 0
                for cri in range(sr, 2):
                    if cri+ri > len(sa)-1:
                        continue
                    for csi in range(ss, 2):
                        if cri == 0 and csi == 0:
                            continue
                        if si+csi > len(r)-1:
                            continue
                        if sa[ri+cri][si+csi] == '#':
                            occ += 1
                if occ == 0:
                    row_arr.append('#')
                else:
                    row_arr.append(s)
                continue
        seata.append(row_arr)
    if seata == sa:
        seat_arrangement = seata
        return
    else:
        seat_arr(seata)

seat_arr(seats_test)
print(f"Part 1 test: {sum(x.count('#') for x in seat_arrangement)}")

seat_arr(seats)
print(f"Part 1: {sum(x.count('#') for x in seat_arrangement)}")

directions = {'w': [-1, 0], 'nw': [-1, -1], 'n': [0, -1], 'ne': [1, -1], 'e': [1, 0], 'se': [1, 1], 's': [0, 1], 'sw': [-1, 1]}

def new_seat_arr(sa):
    global seat_arrangement
    seata = copy.deepcopy(sa)
    for ri, r in enumerate(sa):
        for si, s in enumerate(r):
            occ = 0
            if s == '.':
                continue
            for direct in directions:
                if occ == 5:
                    break
                tsi, tri = directions[direct]
                test_r = ri + tri
                test_s = si + tsi
                while 0 <= test_r <= len(sa)-1 and 0 <= test_s <= len(r)-1:
                    if sa[test_r][test_s] == 'L':
                        break
                    elif sa[test_r][test_s] == '#':
                        occ += 1
                        break
                    test_r += tri
                    test_s += tsi
            if s == '#' and occ < 5:
                continue
            elif s == '#' and occ == 5:
                seata[ri][si] = 'L'
                continue
            elif s == 'L' and occ == 0:
                seata[ri][si] = '#'
                continue
            elif s == 'L' and occ > 0:
                continue
    if seata == sa:
        seat_arrangement = seata
        return
    else:
        new_seat_arr(seata)

new_seat_arr(seats_test)
print(f"Part 2 test: {sum(x.count('#') for x in seat_arrangement)}")

new_seat_arr(seats)
print(f"Part 2: {sum(x.count('#') for x in seat_arrangement)}")