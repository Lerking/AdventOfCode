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
altered_bootcode = []

for l in test_data:
    cc = l.strip('\n')
    c = cc.split()
    c.append(False) #Halt code
    c.append(False) #Altered instruction
    if c[0] == 'nop' or c[0] == 'jmp':
        c.append(c[0]) #Store original instruction
    test_bootcode.append(c)

with open(wd+'/boot_code.txt', 'r') as ER:
    for l in ER:
        cc = l.strip('\n')
        c = cc.split()
        c.append(False) #Halt code
        c.append(False) #Altered instruction
        if c[0] == 'nop' or c[0] == 'jmp':
            c.append(c[0]) #Store original instruction
        bootcode.append(c)

accumulator = 0
halt = False
index = 0
exit_status_ok = False
part_1_done = False

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
    if dat[index][2] == True: #If halt flag is True
        halt = True #Set global Halt flag to True
        return
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

def alter_code(dat):
    for i in dat:
        if i[0] == 'nop' and i[3] == False and i[1] != '+0': #Jump to index +0 would enter an infinite loop - We want to avoid that.
            i[0] = 'jmp' #Change instruction to 'jmp'
            i[3] = True #Set changed flag to True
            return
        elif i[0] == 'jmp' and i[3] == False: #If instruction is 'jmp' and it haven't previously been changed
            i[0] = 'nop' #Change instruction to 'nop'
            i[3] = True #Set changed flag to True
            return

def reset_code(dat):
    for i in dat:
        if i[0] == 'nop' or i[0] == 'jmp':
            i[0] = i[4]

def reset_halt(dat):
    for i in dat:
        i[2] = False #Reset Halt flag

while halt != True:
    execute(test_bootcode)

print(f'Part 1 test: {accumulator}')

reset()
while halt != True:
    execute(bootcode)

print(f'Part 1: {accumulator}')

part_1_done = True

reset()
reset_halt(test_bootcode)
while index <= len(test_bootcode)-1:
    if halt != True:
        execute(test_bootcode)
    if halt == True:
        reset_code(test_bootcode)
        reset_halt(test_bootcode)
        alter_code(test_bootcode)
        reset()
        halt == False

print(f'Part 2 test: {accumulator}')

reset()
reset_halt(bootcode)
while index <= len(bootcode)-1:
    if halt != True:
        execute(bootcode)
    if halt == True:
        reset_code(bootcode)
        reset_halt(bootcode)
        alter_code(bootcode)
        reset()
        halt == False

print(f'Part 2: {accumulator}')