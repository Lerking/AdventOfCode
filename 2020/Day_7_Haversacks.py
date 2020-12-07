test_data = ['light red bags contain 1 bright white bag, 2 muted yellow bags.\n',
            'dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n',
            'bright white bags contain 1 shiny gold bag.\n',
            'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n',
            'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n',
            'dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n',
            'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n',
            'faded blue bags contain no other bags.\n',
            'dotted black bags contain no other bags.\n']

wd = '/home/jan/projects/AdventOfCode/2020'

haversacks = []

with open(wd+'/haversacks.txt', 'r') as ER:
    for l in ER:
        haversacks.append(l)


def read_rules(dat):
    result = []
    for r in dat:
        temp = []
        temp_1 = {}
        td = 0
        tmp = ""
        r.strip('\n')
        rr, cc = r.split('contain')
        bag = rr.split()[:2] #Grab first 2 words
        temp.append('_'.join(bag))
        if not ',' in cc:
            tmp = cc.split()
            if tmp[:1][0].isdigit():
                td = int(tmp[:1][0])
                tmp = '_'.join(tmp[1:3])
                temp_1[tmp] = td
                temp.append(temp_1)
                result.append(temp)
                continue
            if tmp[:1][0] == 'no':
                temp.append(temp_1)
                result.append(temp)
                continue
        else:
            for c in cc.split(','):
                tmp = c.split()
                if tmp[:1][0].isdigit():
                    td = int(tmp[:1][0])
                    tmp = '_'.join(tmp[1:3])
                    temp_1[tmp] = td
        temp.append(temp_1)
        result.append(temp)
    return result

lst = []
def bag_count(tst, bag):
    temp = []
    for b in tst:
        if bag in b[1]:
            temp.append(b[0])
            temp += bag_count(tst, b[0])
    return temp
            
test = read_rules(test_data)
print(f'Part 1 test: {len(bag_count(test, "shiny_gold"))}')

data = read_rules(haversacks)
lst = set(bag_count(data, "shiny_gold"))
print(f'Part 1: {len(lst)}')

def bag_contents(tst, bag):
    cnt = 0
    for b in tst:
        if b[0] == bag:
            cnt += sum(b[1].values())
            for c in list(b[1].keys()):
                cnt += b[1][c] * bag_contents(tst, c)
    return cnt

cnt = bag_contents(test, 'shiny_gold')
print(f'Part 2 test: {cnt}')

cnt = bag_contents(data, 'shiny_gold')
print(f'Part 2: {cnt}')