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

with open(wd+'\\passports.txt', 'r') as ER:
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
    if not 1920 <= int(v['byr']) <= 2020:
        continue
    if not 2010 <= int(v['iyr']) <= 2020:
        continue
    if not 2020 <= int(v['eyr']) <= 2030:
        continue
    if not v['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        continue
    if not v['hcl'].startswith('#') \
        and not all(c in '0123456789abcdef' for c in v['hcl'][1:]) \
        and not len(v['hcl']) == 7:
        continue
    if not all(d in '0123456789' for d in v['pid']) \
        and not len(v['pid']) == 9:
        continue
    if v['hgt'].endswith('in'):
        heads, tail = v['hgt'].rsplit('in')
        if not 59 <= int(heads) <= 76:
            continue
    if v['hgt'].endswith('cm'):
        heads, tail = v['hgt'].rsplit('cm')
        if not 150 <= int(heads) <= 193:
            continue
    valid += 1
    new_valids.append(v)
        
all = [f for f in valids if all(f in valids for k in ['byr', 'iyr', 'eyr', 'pid', 'ecl', 'hcl', 'hgt'])]
byr_valids = [v for v in valids if 1920 <= int(v['byr']) <= 2002]
print(len(byr_valids))
iyr_valids = [v for v in byr_valids if 2010 <= int(v['iyr']) <= 2020]
print(len(iyr_valids))
eyr_valids = [v for v in iyr_valids if 2020 <= int(v['eyr']) <= 2030]
print(len(eyr_valids))
ecl_valids = [v for v in eyr_valids if v['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']]
print(len(ecl_valids))
hcl_valids = [v for v in ecl_valids if re.match('^#[0-9a-f]{6}$', v['hcl'])]
print(hcl_valids)
print(len(hcl_valids))
pid_valids = [v for v in hcl_valids if re.match('[0-9]{9}', v['pid'])]
print(len(pid_valids))
dat = [v['hgt'] for v in pid_valids]
print(len(dat))
print(dat)
hgt_valids = 0
for elm in dat:
    if elm.endswith('in'):
        heads, tail = elm.rsplit('in')
        if 59 <= int(heads) <= 76:
            hgt_valids += 1
    if elm.endswith('cm'):
        heads, tail = elm.rsplit('cm')
        if 150 <= int(heads) <= 193:
            hgt_valids += 1
print(hgt_valids)