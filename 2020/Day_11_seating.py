from collections import Counter

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

seat_arr(seats)

print(f"Part 1: {sum(x.count('#') for x in seat_arrangement)}")