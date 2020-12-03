
tree_map = []
wd = 'C:\\Users\\dksojlg\\projects\\AdventOfCode\\2020'

with open(wd+'\\tree_map.txt', 'r') as ER:
    for item in ER:
        tree_map.append(item.strip('\n'))

line_len = len(tree_map[0])
map_len = len(tree_map)-1 #In order to not go beyond the map, we subtract 1 (remember indices starts at 0)

def traverse(right, down):
    line, col = 0, 0 # Start at top left corner of the map
    trees = 0
    while line < map_len: # As long as we're inside the map, we go on.
        col += right # Accumulate column index
        line += down # Accumulate line index
        if col > line_len-1: # If col is larger than the lenght of the map line
            col = col % line_len # We re-calculate the col index as modulo col/line length (this gives us the remainder, which is our new col index)
        if tree_map[line][col] == '#': # If we encounter a tree, represented as '#' in the map
            trees += 1 # We increase the number of trees we have encounted
    return trees # When the end of the map has been reached, we return the number of trees encounted

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