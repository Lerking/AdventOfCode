test_data = ['F10', 
            'N3',
            'F7',
            'R90',
            'F11']

nav = []
for n in test_data:
    navl = []
    navl.append(n[0:1])
    navl.append(int(n[1:]))
    nav.append(navl)

with open('navigation.txt', 'r') as N:
    navi = [l.strip() for l in N.readlines()]

def manhattan_distance(navi):
    ship_direction = 'east'
    h, v = 0, 0
    for n in navi:
        if n[0] == 'F':
            if ship_direction == 'east':
                h += n[1]
                continue
            elif ship_direction == 'south':
                v -= n[1]
                continue
            elif ship_direction == 'west':
                h -= n[1]
                continue
            elif ship_direction == 'north':
                v += n[1]
        elif n[0] == 'N':
            v += n[1]
            continue
        elif n[0] == 'S':
            v -= n[1]
            continue
        elif n[0] == 'E':
            h += n[1]
            continue
        elif n[0] == 'W':
            h -= n[1]
            continue
        elif n[0] == 'R':
            if n[1] == 90:
                if ship_direction == 'east':
                    ship_direction = 'south'
                elif ship_direction == 'south':
                    ship_direction = 'west'
                elif ship_direction == 'west':
                    ship_direction = 'north'
                elif ship_direction == 'north':
                    ship_direction = 'east'
                continue
            elif n[1] == 180:
                if ship_direction == 'east':
                    ship_direction = 'west'
                elif ship_direction == 'south':
                    ship_direction = 'north'
                elif ship_direction == 'west':
                    ship_direction = 'east'
                elif ship_direction == 'north':
                    ship_direction = 'south'
                continue
            elif n[1] == 270:
                if ship_direction == 'east':
                    ship_direction = 'north'
                elif ship_direction == 'south':
                    ship_direction = 'east'
                elif ship_direction == 'west':
                    ship_direction = 'south'
                elif ship_direction == 'north':
                    ship_direction = 'west'
                continue
        elif n[0] == 'L':
            if n[1] == 90:
                if ship_direction == 'east':
                    ship_direction = 'north'
                elif ship_direction == 'south':
                    ship_direction = 'east'
                elif ship_direction == 'west':
                    ship_direction = 'south'
                elif ship_direction == 'north':
                    ship_direction = 'west'
                continue
            elif n[1] == 180:
                if ship_direction == 'east':
                    ship_direction = 'west'
                elif ship_direction == 'south':
                    ship_direction = 'north'
                elif ship_direction == 'west':
                    ship_direction = 'east'
                elif ship_direction == 'north':
                    ship_direction = 'south'
                continue
            elif n[1] == 270:
                if ship_direction == 'east':
                    ship_direction = 'south'
                elif ship_direction == 'south':
                    ship_direction = 'west'
                elif ship_direction == 'west':
                    ship_direction = 'north'
                elif ship_direction == 'north':
                    ship_direction = 'east'
                continue
    return abs(h)+abs(v)

print(f'Part 1 test: {manhattan_distance(nav)}')

nav = []
for n in navi:
    navl = []
    navl.append(n[0:1])
    navl.append(int(n[1:]))
    nav.append(navl)

print(f'Part 1: {manhattan_distance(nav)}')