'''
Read expence_report.txt
Part 1: Looping through adding 2 numbers until the result is 2021!
Then multiply these 2 numbers, to get the expence report result.
Part 2: Looping through adding 3 numbers until the result is 2021!
Then multiply these 3 numbers, to get the expence report result.
'''

expence_report = []
wd = 'C:\\Users\\dksojlg\\projects\\AdventOfCode\\2020'

with open(wd+'\\expence_report.txt', 'r') as ER:
    for item in ER:
        expence_report.append(int(item))

'''
Part 1
'''
print(expence_report)
index = 0
index_1 = 0
num1 = 0
num2 = 0
result = 0
for x in expence_report:
    for y in expence_report:
        if index_1 == index:
            index_1 += 1
            continue
        if x+y == 2020:
            num1 = x
            num2 = y
            result = x*y
            break
            break
        index_1 += 1
    index_1 = 0
    index += 1

print(index, index_1)
print(f'Num 1 : {num1}, Num2 : {num2} -> result : {result}')

'''
Part 2
'''
index = 0
index_1 = 0
index_2 = 0
num1 = 0
num2 = 0
num3 = 0
result = 0
for x in expence_report:
    for y in expence_report:
        if index_1 == index:
            index_1 += 1
            continue
        for z in expence_report:
            if index_2 == index:
                index_2 += 1
                continue
            if index_2 == index_1:
                index_2 += 1
                continue
            if x+y+z == 2020:
                num1 = x
                num2 = y
                num3 = z
                result = x*y*z
            index_2 += 1
        index_2 = 0
        index_1 += 1
    index_1 = 0
    index_2 = 0
    index += 1

print(index, index_1, index_2)
print(f'Num 1 : {num1}, Num 2 : {num2}, Num 3 : {num3} -> result : {result}')