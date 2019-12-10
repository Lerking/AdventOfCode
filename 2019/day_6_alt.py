test_map = 'COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L'

orbit_list = []
orbits = 0

def orbit(o):
    global orbit_list
    temp = []
    found = False
    for n in o.split(')'):
        if len(orbit_list) > 0:
            if found == False:
                for x in orbit_list:
                    if x[-1] != n:
                        continue
                    elif x[-1] == n:
                        temp = x.copy()
                        found = True
                        break
                    elif len(temp) == 0:
                        found = False
                        temp = orbit_list[-1].copy
                        break
        if found == False:
            temp.append(n)
        else:
            found = False
            continue
            
    return temp

#Testing           
for o in test_map:
    orbit_list.append(orbit(o))

for n in orbit_list:
    orbits += len(n)

print('Total number of orbits in test data: ', orbits-len(orbit_list))

orbit_list = []

#for real
with open('day_6_input.txt', 'r') as F:
    for o in F:
        orbit_list.append(orbit(o.strip('\n')))

for n in orbit_list:
    orbits += len(n)

print('Total number of orbits in real data: ', orbits-len(orbit_list))