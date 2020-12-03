
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

trees = 1

trees *= traverse(1,1)
trees *= traverse(3,1) #Part 1
trees *= traverse(5,1)
trees *= traverse(7,1)
trees *= traverse(1,2)

print(trees)