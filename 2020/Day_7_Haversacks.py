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
    result = [] #Create empty result list
    for r in dat:
        temp = [] #Create empty temporary list
        temp_1 = {} #Create empty temporary dict
        td = 0 #Initiate temporary digit value
        tmp = "" #Initiate temporary child bag name
        r.strip('\n') #Strip '\n' newline char from data line
        rr, cc = r.split('contain') #Split in parent bag and child bags
        bag = rr.split()[:2] #Grab first 2 words
        temp.append('_'.join(bag)) #Join the 2 words of bag with '_', and store in list
        if not ',' in cc: #If there's only 1 child
            tmp = cc.split() #Split child part into words
            if tmp[:1][0].isdigit(): #If 1st word is a digit
                td = int(tmp[:1][0]) #Store digit
                tmp = '_'.join(tmp[1:3]) #Join 2nd and 3rd word of child part with '_'
                temp_1[tmp] = td #Create dict with child word as key and digit as value
                temp.append(temp_1) #Add dict to list
                result.append(temp) #Add list to result list
                continue #Jump to next item in dat
            if tmp[:1][0] == 'no': #If 1st word of child part is 'no'
                temp.append(temp_1) #Add empty dict to list
                result.append(temp) #Add list to result list
                continue #Jump to next item in dat
        else:
            for c in cc.split(','): #If more than 1 child bag, devide them at ','
                tmp = c.split() #Split  child into words
                if tmp[:1][0].isdigit(): #If 1st word is a digit
                    td = int(tmp[:1][0]) #store digit for dict value
                    tmp = '_'.join(tmp[1:3]) #Create child bag name from 2nd and 3rd word
                    temp_1[tmp] = td #Add key, value pair to dict
        temp.append(temp_1) #Add dict to list
        result.append(temp) #Add list to result list
    return result #return result list

def bag_count(tst, bag):
    temp = [] #Initiate empty list
    for b in tst:
        if bag in b[1]: #Check if bag name exists in dict
            temp.append(b[0]) #Add bag name to list
            temp += bag_count(tst, b[0]) #Add next child to list
    return temp #Return list of child bags
            
test = read_rules(test_data) #Creat list from test input
print(f'Part 1 test: {len(bag_count(test, "shiny_gold"))}')

lst = [] #Initiate empty list
data = read_rules(haversacks) #Create list from real input
lst = set(bag_count(data, "shiny_gold")) #Eliminate duplicates from list
print(f'Part 1: {len(lst)}')

def bag_contents(tst, bag):
    cnt = 0 #Initiate temporary counter
    for b in tst:
        if b[0] == bag: #If bag name in tst matches input bag name
            cnt += sum(b[1].values()) #Summarize values in dict
            for c in list(b[1].keys()): #Loop over dict keys as child bag names
                cnt += b[1][c] * bag_contents(tst, c) #Add value of child bag name key times count of next level for child bag name
    return cnt #Return count of current child bag name

cnt = bag_contents(test, 'shiny_gold') #Store final count of recursively traversing child bag names fro test input
print(f'Part 2 test: {cnt}')

cnt = bag_contents(data, 'shiny_gold') #Store final count of recursively traversing child bag names fro real input
print(f'Part 2: {cnt}')