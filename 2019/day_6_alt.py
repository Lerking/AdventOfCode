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

def sorting(o):
    global orbits_list
    global sorted_list
    global raw_temp
    index = 0
    for i in raw_temp:
        if i.split(')')[0] == o:
            sorted_list.append(i)
            del(raw_temp[index])
            orbits_list.append(i.split(')')[1])
            sorting(i.split(')')[1])
        else:
            index += 1
    return
            
#Testing           
for o in test_map:
    orbit_list.append(orbit(o))

for n in orbit_list:
    orbits += len(n)

print('Total number of orbits in test data: ', orbits-len(orbit_list))

raw_temp = []
orbit_list = []
raw_list = []
sorted_list = []
orbits_list = []

#for real
with open('/storage/emulated/0/documents/adventorcode/2019/day_6_input.txt') as F:
#with open('day_6_input.txt', 'r') as F:
    for o in F:
        raw_list.append(o.strip('\n'))

raw_temp = raw_list.copy()

sorting('COM')
print(orbits_list)
sorting(orbits_list[0])
print(sorted_list)
print(len(sorted_list))

for n in orbit_list:
    orbits += len(n)

print('Total number of orbits in real data: ', orbits-len(orbit_list))