'''
Day 2. Help finding valid passwords.
Part 1: Find number of valid passwords in input list, based on first rule set.
Part 2: Find number of valid passwords, based on updated rule set.
'''

wd = 'C:\\Users\\dksojlg\\projects\\AdventOfCode\\2020'
valid_passwords = []
'''
Part 1
Test data:
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Rule set:
part 1, indicates lowest and highest number of instances (1-3).
part 2, the instance (a:).
part 3, the password (abcde).
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
Test data:
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Rule set:
part 1, indicates positions of instance (1-3). 1 and only 1 of the positions must contain
part 2, the instance (a:).
part 3, the password (abcde).
'''
valid_passwords = []
with open(wd+'\\passwords.txt', 'r') as ER:
    for item in ER:
        nn, ins, psw = item.split(" ")
        psw = psw.strip("\n")
        index_1, index_2 = nn.split("-")
        instance = str(ins[0])
        if bool(psw[int(index_1)-1] == instance) ^ bool(psw[int(index_2)-1] == instance):
            valid_passwords.append(psw)

print(f'Valid passwords using second rule set : {len(valid_passwords)}')