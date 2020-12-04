import re

test_data = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n',
            'byr:1937 iyr:2017 cid:147 hgt:183cm\n',
            '\n',
            'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\n',
            'hcl:#cfa07d byr:1929\n',
            '\n',
            'hcl:#ae17e1 iyr:2013\n',
            'eyr:2024\n',
            'ecl:brn pid:760753108 byr:1931\n',
            'hgt:179cm\n',
            '\n',
            'hcl:#cfa07d eyr:2025 pid:166559648\n',
            'iyr:2011 ecl:brn hgt:59in\n']

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
print(f'Number of valid passports : {len(valids)}')

valid = 0
new_valids = []
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
    new_valids.append(v)
print(len(new_valids))
