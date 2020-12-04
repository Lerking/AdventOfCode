import re

wd = 'C:\\Users\\dksojlg\\projects\\AdventOfCode\\2020'

with open('/home/jan/projects/AdventOfCode/2020/passports.txt', 'r') as ER:
    passports = []
    passport = {}
    for item in ER:
        if item == "\n":
            passports.append(passport)
            passport = {}
            continue
        for elm in item.split(' '):
            key, val = elm.split(':')
            passport[key] = val.strip('\n')
passports.append(passport)

valids = [v for v in passports if len(v) == 8 or len(v) == 7 and 'cid' not in v]
print(f'Part 1 : {len(valids)}')

valid = 0
for v in valids:
    if not 1920 <= int(v['byr']) <= 2002:
        continue
    if not 2010 <= int(v['iyr']) <= 2020:
        continue
    if not 2020 <= int(v['eyr']) <= 2030:
        continue
    if not re.match('[amb|blu|brn|gry|grn|hzl|oth]', v['ecl']):
        continue
    if not re.match('^#[0-9a-f]{6}', v['hcl']):
        continue
    if not len(v['pid']) == 9 or not re.match('[0-9]{9}', v['pid']):
        continue
    if not v['hgt'].endswith('in') and not v['hgt'].endswith('cm'):
        continue
    if v['hgt'].endswith('in'):
        heads, tail = v['hgt'].rsplit('in')
        if not len(v['hgt']) == 4 or not 59 <= int(heads) <= 76:
            continue
    if v['hgt'].endswith('cm'):
        heads, tail = v['hgt'].rsplit('cm')
        if not len(v['hgt']) == 5 or not 150 <= int(heads) <= 193:
            continue
    valid += 1
print(f'Part 2 : {valid}')
