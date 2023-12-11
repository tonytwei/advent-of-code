f = open("input.txt", "r")
#f = open("test1.txt", "r")
lines = f.readlines()
lines = [line.split('\n')[0] for line in lines]

grid = [[char for char in line] for line in lines]

emptyRows = set(range(len(grid)))
emptyCols = set(range(len(grid[0])))
for row, line in enumerate(grid):
    for col, char in enumerate(line):
        if char == '#':
            # ensures not in set
            if row in emptyRows:
                emptyRows.remove(row)
            if col in emptyCols:
                emptyCols.remove(col)

emptyCols = list(emptyCols)
emptyCols.sort(reverse=True)
for emptyCol in emptyCols:
    for row, line in enumerate(grid):
        line.insert(emptyCol, '.')

emptyRows = list(emptyRows)
emptyRows.sort(reverse=True)
for emptyRow in emptyRows:
    grid.insert(emptyRow, ['.' for _ in grid[0]])

positions = []
for row, line in enumerate(grid):
    for col, char in enumerate(line):
        if char == "#":
            positions.append((row, col))

res = 0
while len(positions) > 0:
    startRow, startCol = positions.pop(0)
    for endRow, endCol in positions:
        rowDiff = abs(endRow - startRow)
        colDiff = abs(endCol - startCol)
        res += rowDiff
        res += colDiff
print(res)