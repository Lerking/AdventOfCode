import re

wd = '/home/jan/projects/AdventOfCode/2015'

def regex_cnt(string, pattern):
    return len(re.findall(pattern, string))

strings = ['ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']

nice_list = []
naughty_list = []

def string_nice(s):
    if not regex_cnt(s, '[aeiou]') >= 3:
        naughty_list.append(s)
        return
    if not re.search('aa|bb|cc|dd|ee|ff|gg|hh|ii|jj|kk|ll|mm|nn|oo|pp|qq|rr|ss|tt|uu|vv|ww|xx|yy|zz', s):
        naughty_list.append(s)
        return
    if re.search('ab|cd|pq|xy', s):
        naughty_list.append(s)
        return
    else:
        nice_list.append(s)
        return

for s in strings:
    string_nice(s)

print("Part 1 tests:")
print(f'Nice strings: {len(nice_list)}')
print(f'Naughty strings: {len(naughty_list)}')

input_list = []

with open(wd+"/naughty_list.txt", 'r') as F:
    for l in F:
        input_list.append(l.strip('\n'))

new_strings = ['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']
nice_list = []
naughty_list = []

def new_nice(s):
    if not re.findall(r"([a-z]{2}).*?(\1)", s):
        naughty_list.append(s)
        return
    if not re.search('a.a|b.b|c.c|d.d|e.e|f.f|g.g|h.h|i.i|j.j|k.k|l.l|m.m|n.n|o.o|p.p|q.q|r.r|s.s|t.t|u.u|v.v|w.w|x.x|y.y|z.z', s):
        naughty_list.append(s)
        return
    else:
        nice_list.append(s)
        return

for s in new_strings:
    new_nice(s)

print("Part 2 test:")
print(f'Nice strings: {len(nice_list)}')
print(f'Naughty strings: {len(naughty_list)}')

nice_list = []
naughty_list = []

for s in input_list:
    new_nice(s)

print("Part 2:")
print(f'Nice strings: {len(nice_list)}')
print(f'Naughty strings: {len(naughty_list)}')