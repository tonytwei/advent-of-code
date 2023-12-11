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
            # solves key error
            emptyRows.add(row)
            emptyRows.remove(row)
            emptyCols.add(col)
            emptyCols.remove(col)

emptyCols = list(emptyCols)
emptyRows = list(emptyRows)

positions = []
for row, line in enumerate(grid):
    for col, char in enumerate(line):
        if char != "#":
            continue

        gRow = gCol = 0
        for emptyRow in emptyRows:
            if row > emptyRow:
                gRow += 1
        for emptyCol in emptyCols:
            if col > emptyCol:
                gCol += 1
        positions.append((row, col, gRow, gCol))

res = 0
MULTIPLIER = 1000000
steps = MULTIPLIER - 1
while len(positions) > 0:
    startRow, startCol, gStartRow, gStartCol = positions.pop(0)
    for endRow, endCol, gEndRow, gEndCol in positions:
        rowDiff = abs(endRow - startRow)
        colDiff = abs(endCol - startCol)
        gRowDiff = abs(gEndRow - gStartRow)
        gColDiff = abs(gEndCol - gStartCol)
        res += rowDiff + colDiff
        res += steps * (gRowDiff + gColDiff)
print(res)