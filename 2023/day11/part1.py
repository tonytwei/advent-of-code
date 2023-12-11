#f = open("input.txt", "r")
f = open("test1.txt", "r")
lines = f.readlines()
lines = [line.split('\n')[0] for line in lines]

grid = [[char for char in line] for line in lines]

emptyRows = set(range(len(grid)))
emptyCols = set(range(len(grid[0])))
for row, line in enumerate(grid):
    for col, char in enumerate(line):
        if char == '#':
            # solves key error
            emptyRows.add(row)
            emptyRows.remove(row)
            emptyCols.add(col)
            emptyCols.remove(col)

print(emptyRows)
print(emptyCols)
l = list(range(10))
l.insert(5, '.')
print(l)
l = [l]
print(l)

for emptyCol in emptyCols:
    for row in enumerate(l):
        row.insert(emptyCol, '.')
print(l)