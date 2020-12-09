test_data = [35, 20, 15, 25, 47,
            40, 62, 55, 65, 95,
            102, 117, 150, 182, 127,
            219, 299, 277, 309, 576]

xmas = []

wd = '/home/jan/projects/AdventOfCode/2020'

with open(wd+'/xmas_input.txt', 'r') as ER:
    for item in ER:
        xmas.append(int(item.strip('\n')))

def get_fault(preample, dat):
    data = dat.copy()
    found = False
    while len(data) > preample:
        for index in range(0, preample):
            for index_1 in range(0, preample):
                if index_1 == index:
                    continue
                if data[index]+data[index_1] == data[preample]:
                    found = True
                    break
                found = False
            if found == True:
                data.pop(0)
                break
        if found == False:
            break
    
    return data[preample]

def weakness(fault, dat):
    tmp = []
    for n in dat:
        if sum(tmp) == fault:
            return min(tmp)+max(tmp)
        tmp.append(n)
        if len(tmp) < 3:
            continue
        elif sum(tmp) < fault:
            continue
        else:
            while sum(tmp) > fault:
                tmp.pop(0)

print(f'Part 1 test: {get_fault(5, test_data)}')

print(f'Part 1: {get_fault(25, xmas)}')

print(f'Part 2 test: {weakness(get_fault(5, test_data), test_data)}')

print(f'Part 2: {weakness(get_fault(25, xmas), xmas)}')