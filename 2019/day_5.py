test_prg1 = [3,0,4,0,99]
test_prg2 = [1002,4,3,4,33]
test_prg3 = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
            1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
            999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
test1_inputs = [0,1,2,3,4,5,6,7,8,9]

def prg(pg, i):
    index = 0
    oc = pg.copy()
    retval = 0
    has_retval = False
    program_running = True
    while program_running == True:
        debug_oc = oc[index:10+index]
        if len(str(oc[index])) <= 2:
            if oc[index] == 99:
                if has_retval == True:
                    return retval
                else:
                    program_running = False
                    break
            elif oc[index] == 1:
                oc[oc[index+3]]=oc[oc[index+1]]+oc[oc[index+2]]
                index += 4
                continue
            elif oc[index] == 2:
                oc[oc[index+3]]=oc[oc[index+1]]*oc[oc[index+2]]
                index += 4
                continue
            elif oc[index] == 3:
                oc[oc[index+1]]=i
                index += 2
                continue
            elif oc[index] == 4:
                #print(oc[oc[index+1]])
                retval = oc[oc[index+1]]
                has_retval = True
                index += 2
                continue
        elif len(str(oc[index])) > 2:
            if oc[index] - 10000 >= 1:
                pm = str(oc[index])[:3]     # First 3 digits are parameter modes
                opcode = str(oc[index])[2:]     # Last 2 digits is the opcode
            elif oc[index] - 1000 >= 1:
                pm = str(oc[index])[:2]     # First 2 digits are parameter modes
                opcode = str(oc[index])[2:]     # Last 2 digits is the opcode
            elif oc[index] - 100 >= 1:
                pm = str(oc[index])[0]     # First digit is parameter mode
                opcode = str(oc[index])[2]     # Last 2 digits is the opcode
            if opcode == '01' or opcode == '1':
                if pm == '11': # Both parameter modes are immediate
                    oc[oc[index+3]]=oc[index+1]+oc[index+2]
                    index += 4
                    continue
                elif pm == '01' or pm == '1': # First parameter mode is immediate, second is position
                    oc[oc[index+3]]=oc[index+1]+oc[oc[index+2]]
                    index += 4
                    continue
                elif pm == '10': # First parameter mode is position, second is immediate
                    oc[oc[index+3]]=oc[oc[index+1]]+oc[index+2]
                    index += 4
                    continue
                elif pm == '00':   # Both parameter modes are position
                    oc[oc[index+3]]=oc[oc[index+1]]+oc[oc[index+2]]
                    index += 4
                    continue
            elif opcode == '02' or opcode == '2':
                if pm == '11': # Both parameter modes are immediate
                    oc[oc[index+3]]=oc[index+1]*oc[index+2]
                    index += 4
                    continue
                elif pm == '01' or pm == '1': # First parameter mode is immediate, second is position
                    oc[oc[index+3]]=oc[index+1]*oc[oc[index+2]]
                    index += 4
                    continue
                elif pm == '10': # First parameter mode is position, second is immediate
                    oc[oc[index+3]]=oc[oc[index+1]]*oc[index+2]
                    index += 4
                    continue
                elif pm == '00':   # Both parameter modes are position
                    oc[oc[index+3]]=oc[oc[index+1]]*oc[oc[index+2]]
                    index += 4
                    continue
            if opcode == '04' or opcode == '4':
                if pm == '1': # Parameter mode is immediate
                    #print(oc[index+1])
                    retval = oc[index+1]
                    has_retval = True
                    index += 2
                    continue
                elif pm == '0': # Parameter mode is position
                    #print(oc[oc[index+1]])
                    retval = oc[oc[index+1]]
                    has_retval = True
                    index += 2
                    continue
            if opcode == '03' or opcode == '3':
                if pm == '1': # Parameter mode is immediate
                    oc[index+1]=i
                    index += 2
                    continue
                elif pm == '0': # Parameter mode is position
                    oc[oc[index+1]]=i
                    index += 2
                    continue
            if opcode == '05' or opcode == '5':
                if pm == '00':
                    if oc[oc[index+1]] != 0:
                        index = oc[oc[index+2]]
                        continue
                    index += 3
                    continue
                if pm == '10':
                    if oc[oc[index+1]] != 0:
                        index = oc[index+2]
                        continue
                    index += 3
                    continue
                if pm == '01':
                    if oc[index+1] != 0:
                        index = oc[oc[index+2]]
                        continue
                    index += 3
                    continue
                if pm == '11':
                    if oc[index+1] != 0:
                        index = oc[index+2]
                        continue
                    index += 3
                    continue
            if opcode == '06' or opcode == '6':
                if pm == '00':
                    if oc[oc[index+1]] == 0:
                        index = oc[oc[index+2]]
                        continue
                    index += 3
                    continue
                if pm == '10':
                    if oc[oc[index+1]] == 0:
                        index = oc[index+2]
                        continue
                    index += 3
                    continue
                if pm == '01':
                    if oc[index+1] == 0:
                        index = oc[oc[index+2]]
                        continue
                    index += 3
                    continue
                if pm == '11':
                    if oc[index+1] == 0:
                        index = oc[index+2]
                        continue
                    index += 3
                    continue
            if opcode == '07' or opcode == '7':
                if pm == '0':
                    if oc[index+1] < oc[oc[index+2]]:
                        oc[oc[index+3]] = 1
                    else:
                        oc[oc[index+3]] = 0
                    index += 4
                    continue
                if pm == '1':
                    if oc[index+1] < oc[oc[index+2]]:
                        oc[oc[index+3]] = 1
                    else:
                        oc[oc[index+3]] = 0
                    index += 4
                    continue
                '''
                if pm == '01':
                    if oc[index+1] < oc[oc[index+2]]:
                        oc[oc[index+3]] = 1
                    else:
                        oc[oc[index+3]] = 0
                    index += 4
                    continue
                if pm == '11':
                    if oc[index+1] < oc[index+2]:
                        oc[oc[index+3]] = 1
                    else:
                        oc[oc[index+3]] = 0
                    index += 4
                    continue
                '''
            if opcode == '08' or opcode == '8':
                if pm == '00':
                    if oc[oc[index+1]] == oc[oc[index+2]]:
                        oc[oc[index+3]] = 1
                    else:
                        oc[oc[index+3]] = 0
                    index += 4
                    continue
                if pm == '10':
                    if oc[oc[index+1]] == oc[index+2]:
                        oc[oc[index+3]] = 1
                    else:
                        oc[oc[index+3]] = 0
                    index += 4
                    continue
                if pm == '01':
                    if oc[index+1] == oc[oc[index+2]]:
                        oc[oc[index+3]] = 1
                    else:
                        oc[oc[index+3]] = 0
                    index += 4
                    continue
                if pm == '11':
                    if oc[index+1] == oc[index+2]:
                        oc[oc[index+3]] = 1
                    else:
                        oc[oc[index+3]] = 0
                    index += 4
                    continue
        else:           
            program_running = False
            return retval
    return oc

for t in test1_inputs:
    i = t
    r = prg(test_prg1, i)
    if r != t:
        print('Test failed - Expected:', i,' Received:', t)
    else:
        print('Test passed!')

r = prg(test_prg2, 0)
t = [1002,4,3,4,99]
if r != t:
    print('Test failed - Expected:', t,' Received:', r)
else:
    print('Test passed!')

r = prg(test_prg3, 7)
t = 999
if r != t:
    print('Test failed - Expected:', t,' Received:', r)
else:
    print('Test passed!')

r = prg(test_prg3, 8)
t = 1000
if r != t:
    print('Test failed - Expected:', t,' Received:', r)
else:
    print('Test passed!')

r = prg(test_prg3, 9)
t = 1001
if r != t:
    print('Test failed - Expected:', t,' Received:', r)
else:
    print('Test passed!')

# Going for real
with open('day_5_input.txt', 'r') as F:
    program = []
    for w in F:
        for n in w.split(','):
            program.append(int(n.strip('\n')))

diagnostic_code = prg(program, 5)
print(diagnostic_code)

