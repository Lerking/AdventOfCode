orig_OPCODES = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,
            2,10,1,19,1,5,19,23,1,23,5,27,2,27,10,31,
            1,5,31,35,2,35,6,39,1,6,39,43,2,13,43,47,
            2,9,47,51,1,6,51,55,1,55,9,59,2,6,59,63,
            1,5,63,67,2,67,13,71,1,9,71,75,1,75,9,79,
            2,79,10,83,1,6,83,87,1,5,87,91,1,6,91,95,
            1,95,13,99,1,10,99,103,2,6,103,107,1,107,5,111,
            1,111,13,115,1,115,13,119,1,13,119,123,2,123,13,127,
            1,127,6,131,1,131,9,135,1,5,135,139,2,139,6,143,
            2,6,143,147,1,5,147,151,1,151,2,155,1,9,155,0,
            99,
            2,14,0,0]

OPCODES = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,
            2,10,1,19,1,5,19,23,1,23,5,27,2,27,10,31,
            1,5,31,35,2,35,6,39,1,6,39,43,2,13,43,47,
            2,9,47,51,1,6,51,55,1,55,9,59,2,6,59,63,
            1,5,63,67,2,67,13,71,1,9,71,75,1,75,9,79,
            2,79,10,83,1,6,83,87,1,5,87,91,1,6,91,95,
            1,95,13,99,1,10,99,103,2,6,103,107,1,107,5,111,
            1,111,13,115,1,115,13,119,1,13,119,123,2,123,13,127,
            1,127,6,131,1,131,9,135,1,5,135,139,2,139,6,143,
            2,6,143,147,1,5,147,151,1,151,2,155,1,9,155,0,
            99,
            2,14,0,0]

mem = []

test = list(orig_OPCODES)

zero_op_opcodes = {'0099' : end}
one_op_opcodes = {'0003' : inpt, '0004' : outpt}
three_op_opcodes = {'0001' : add, '0002' : mul}

#operand types
positional = 0
immediate = 1

ip = 0 #instruction pointer/program counter
ip_adjust = 0
proc_cycle = 0

def fetch():
    return decode(str(OPCODE[ip]).zfill(4))

    
def decode(instr):
    global ip_adjust
    if instr in zero_op_opcodes:
        ip_adjust = 1
    elif instr in three_op_opcodes:
        ip_adjust = 4
    return execute(instr)

def execute(instr):
    if instr[0] == '0':
        op1 = positional
    elif instr[0] == '1':
        op1 = immediate
    if instr[1] == '0':
        op2 = positional
    elif instr[1] == '1':
        op2 = immediate
    if instr[:2] == '01':
        add(op1, op2)
        
def prg(oc, i):
    index = i
    programm_running = True
    while programm_running == True:
        if oc[index] == 99:
            program_running = False
            break
        elif oc[index] == 1:
            oc[oc[index+3]]=oc[oc[index+1]]+oc[oc[index+2]]
            index+=4
            continue
        elif oc[index] == 2:
            oc[oc[index+3]]=oc[oc[index+1]]*oc[oc[index+2]]
            index+=4
            continue
        else:           
            program_running = False
            return False
    return oc

print(prg(OPCODES, 0))  #day 2 part 1

result = 19690720

for noun in range(100):
    test[1]=noun
    for verb in range(100):
        test[2]=verb
        res = prg(test, 0)
        if res == False:
            test = list(orig_OPCODES)
            test[1]=noun
            test[2]=verb
            continue
        elif res[0] == result:
            calc = 100*noun+verb
            print(calc)   #day2 part 2
            break
            break
        else:
            test = list(orig_OPCODES)
            test[1]=noun
            test[2]=verb
            continue