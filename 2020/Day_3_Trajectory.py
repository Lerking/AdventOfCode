
tree_map = []
wd = 'C:\\Users\\dksojlg\\projects\\AdventOfCode\\2020'

with open(wd+'\\tree_map.txt', 'r') as ER:
    for item in ER:
        tree_map.append(item.strip('\n'))

line_len = len(tree_map[0])
map_len = len(tree_map)-1

def traverse(right, down):
    line, col = 0, 0
    trees = 0
    while line < map_len:
        col += right
        line += down
        if col > line_len-1:
            col = col % line_len
        if tree_map[line][col] == '#':
            trees += 1
    return trees

'''
Part 1
Traject right 3, down 1
'''
print(f'Part 1 - Number of trees encountered : {traverse(3,1)}')

'''
Part 2
Trajections:
right 1, down 1
right 3, down 1
right 5, down 1
right 7, down 1
right 1, down 2
multiply encountered trees in all trajections.
'''

trees = 1

trees *= traverse(1,1)
trees *= traverse(3,1)
trees *= traverse(5,1)
trees *= traverse(7,1)
trees *= traverse(1,2)

print(f'Part 2 - Multiplied number of encountered trees : {trees}')