from enum import Enum

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

pg1 = [1,9,10,3,2,3,11,0,99,30,40,50]
pg2 = [1,0,0,0,99]
pg3 = [2,3,0,3,99]
pg4 = [2,4,4,5,99,0]
pg5 = [1,1,1,4,99,5,6,0,99]

mem = []

test = list(orig_OPCODES)

class cycle(Enum):
    HALT = 0
    FETCH = 1
    EXECUTE = 2
    INIT = 5
    ERROR = -1

def end():
    global state
    state = cycle.HALT
    return

def inpt(op):
    global mem
    return

def outpt(op):
    return

def add(op1, op2):
    if op1 == positional and op2 == positional:
        mem[mem[ip+3]] = int(mem[mem[ip+1]]) + int(mem[mem[ip+2]])
    elif op1 == positional and op2 == immediate:
        mem[mem[ip+3]] = int(mem[mem[ip]]) + int(mem[ip+2])
    elif op1 == immediate and op2 == positional:
        mem[mem[ip+3]] = int(mem[ip+1]) + int(mem[mem[ip+2]])
    else:
        mem[mem[ip+3]] = int(mem[ip+1]) + int(mem[ip+2])
    return

def mul(op1, op2):
    if op1 == positional and op2 == positional:
        mem[mem[ip+3]] = int(mem[mem[ip+1]]) * int(mem[mem[ip+2]])
    elif op1 == positional and op2 == immediate:
        mem[mem[ip+3]] = int(mem[mem[ip]]) * int(mem[ip+2])
    elif op1 == immediate and op2 == positional:
        mem[mem[ip+3]] = int(mem[ip+1]) * int(mem[mem[ip+2]])
    else:
        mem[mem[ip+3]] = int(mem[ip+1]) * int(mem[ip+2])
    return

zero_op_opcodes = {'99' : end}
one_op_opcodes = {'03' : inpt, '04' : outpt}
three_op_opcodes = {'01' : add, '02' : mul}

#operand types
positional = 0
immediate = 1

state = cycle.INIT
ip = 0 #instruction pointer/program counter
ip_adjust = 0
running = True

def reset(): #initial state
    global state
    global ip
    global ip_adjust
    global running
    global mem
    mem = []
    state = cycle.INIT
    ip = 0 #instruction pointer/program counter
    ip_adjust = 0
    running = True

def fetch(pg):
    if type(pg) != str:
        pg = str(pg).zfill(4)
    decode(pg)
    
def decode(instr):
    global ip_adjust
    if instr[2:] in zero_op_opcodes:
        ip_adjust = 1
    elif instr[2:] in three_op_opcodes:
        ip_adjust = 4
    return execute(instr)

def execute(instr):
    global ip
    global state
    if instr[0] == '0':
        op1 = positional
    elif instr[0] == '1':
        op1 = immediate
    if instr[1] == '0':
        op2 = positional
    elif instr[1] == '1':
        op2 = immediate
    if instr[2:] == '01':
        add(op1, op2)
    elif instr[2:] == '02':
        mul(op1, op2)
    elif instr[2:] == '03':
        inpt(op1)
    elif instr[2:] == '04':
        outpt(op1)
    elif instr[2:] == '99':
        end()
    else:
        state = cycle.ERROR
        return
    ip += ip_adjust
    return

def init(pg):
    global state
    global mem
    index = 0
    op_index = 0
    for n in pg:
        if index == 0 or index == op_index:
            tmp = str(pg[index]).zfill(4)
            if tmp[2:] in one_op_opcodes:
                op_index += 1
            elif tmp[2:] in three_op_opcodes:
                op_index += 4
            mem.append(tmp)
            index += 1
            continue
        else:
            mem.append(pg[index])
            index += 1
    state = cycle.EXECUTE

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

if __name__ == "__main__":
    reset()
    while running == True:
        if state == cycle.INIT:
            init(pg1)
        elif state == cycle.EXECUTE:
            fetch(mem[ip])
        elif state == cycle.HALT:
            running = False
            print(mem)
            assert mem[3] == 70
            assert mem[0] == 3500
        elif state == cycle.ERROR:
            pass

    reset()
    while running == True:
        if state == cycle.INIT:
            init(pg2)
        elif state == cycle.EXECUTE:
            fetch(mem[ip])
        elif state == cycle.HALT:
            running = False
            print(mem)
            assert mem[0] == 2
        elif state == cycle.ERROR:
            pass

    reset()
    while running == True:
        if state == cycle.INIT:
            init(pg3)
        elif state == cycle.EXECUTE:
            fetch(mem[ip])
        elif state == cycle.HALT:
            running = False
            print(mem)
            assert mem[3] == 6
        elif state == cycle.ERROR:
            pass

    reset()
    while running == True:
        if state == cycle.INIT:
            init(pg4)
        elif state == cycle.EXECUTE:
            fetch(mem[ip])
        elif state == cycle.HALT:
            running = False
            print(mem)
            assert mem[5] == 9801
        elif state == cycle.ERROR:
            pass

    reset()
    while running == True:
        if state == cycle.INIT:
            init(pg5)
        elif state == cycle.EXECUTE:
            fetch(mem[ip])
        elif state == cycle.HALT:
            running = False
            print(mem)
            assert mem[0] == 30
        elif state == cycle.ERROR:
            pass

    reset()
    while running == True:
        if state == cycle.INIT:
            init(OPCODES)
        elif state == cycle.EXECUTE:
            fetch(mem[ip])
        elif state == cycle.HALT:
            running = False
            print(mem[0])
            assert mem[0] == 9706670
        elif state == cycle.ERROR:
            pass
    
    #print(prg(OPCODES, 0))  #day 2 part 1

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
