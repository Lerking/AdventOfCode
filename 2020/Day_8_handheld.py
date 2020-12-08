test_data = ['nop +0\n',
            'acc +1\n',
            'jmp +4\n',
            'acc +3\n',
            'jmp -3\n',
            'acc -99\n',
            'acc +1\n',
            'jmp -4\n',
            'acc +6\n']

wd = '/home/jan/projects/AdventOfCode/2020'

bootcode = []
test_bootcode = []

for l in test_data:
    cc = l.strip('\n')
    c = cc.split()
    c.append(False)
    test_bootcode.append(c)

with open(wd+'/boot_code.txt', 'r') as ER:
    for l in ER:
        cc = l.strip('\n')
        c = cc.split()
        c.append(False)
        bootcode.append(c)

accumulator = 0
halt = False
index = 0

def reset():
    global accumulator
    global halt
    global index
    accumulator = 0
    halt = False
    index = 0

def execute(dat): #Instruction index
    global accumulator
    global halt
    global index
    if dat[index][2] == True:
        halt = True
    elif dat[index][0] == 'acc':
        accumulator += int(dat[index][1])
        dat[index][2] = True
        index += 1
        return
    elif dat[index][0] == 'nop':
        dat[index][2] = True
        index += 1
        return
    elif dat[index][0] == 'jmp':
        dat[index][2] = True
        index += int(dat[index][1])
        return
    return

while halt != True:
    execute(test_bootcode)

print(f'Part 1 test: {accumulator}')

reset()
while halt != True:
    execute(bootcode)

print(f'Part 1: {accumulator}')