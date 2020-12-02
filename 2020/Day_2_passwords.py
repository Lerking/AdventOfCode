'''
Day 2. Help finding valid passwords.
Part 1: Find number of valid passwords in input list.

'''

wd = 'C:\\Users\\dksojlg\\projects\\AdventOfCode\\2020'
valid_passwords = []
'''
Part 1
'''
with open(wd+'\\passwords.txt', 'r') as ER:
    for item in ER:
        nn, ins, psw = item.split(" ")
        psw = psw.strip("\n")
        minimum, maximum = nn.split("-")
        instance = str(ins[0])
        if int(minimum) <= psw.count(instance) <= int(maximum):
            valid_passwords.append(psw)

print(f'Valid passwords using first rule set : {len(valid_passwords)}')

'''
Part 2
'''
valid_passwords = []
valid = False
with open(wd+'\\passwords.txt', 'r') as ER:
    for item in ER:
        valid_1 = False
        valid_2 = False
        nn, ins, psw = item.split(" ")
        psw = psw.strip("\n")
        index_1, index_2 = nn.split("-")
        instance = str(ins[0])
        if psw[int(index_1)-1] == instance:
            valid_1 = True
        if psw[int(index_2)-1] == instance:
            valid_2 = True
        if valid_1 ^ valid_2:
            valid_passwords.append(psw)

print(f'Valid passwords using second rule set : {len(valid_passwords)}')