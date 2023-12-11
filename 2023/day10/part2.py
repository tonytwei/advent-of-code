f = open("input.txt", "r")
#f = open("test1.txt", "r")
#f = open("test2.txt", "r")
#f = open("test3.txt", "r")
#f = open("test4.txt", "r")
lines = f.readlines()

start = ('row', 'col')

grid = []
for row, line in enumerate(lines):
    line = line.split("\n")[0]
    curRow = []
    for col, char in enumerate(line):
        curRow.append(char)
        if char == "S":
            start = (int(row), int(col))
    grid.append(curRow)

# convert n x m grid to 3n x 3m
# L would be represented as :
# 0 1 0
# 0 1 1
# 0 0 0
newGrid = []
for row, line in enumerate(grid):
    for _ in range(3):
        newGrid.append([])
    newRowStart = 3 * row
    for col, char in enumerate(line):
        newCol = 3 * row
        if char == '|':
            newGrid[newRowStart + 0].extend([0, 1, 0])
            newGrid[newRowStart + 1].extend([0, 1, 0])
            newGrid[newRowStart + 2].extend([0, 1, 0])
        elif char == '-':
            newGrid[newRowStart + 0].extend([0, 0, 0])
            newGrid[newRowStart + 1].extend([1, 1, 1])
            newGrid[newRowStart + 2].extend([0, 0, 0])
        elif char == 'L':
            newGrid[newRowStart + 0].extend([0, 1, 0])
            newGrid[newRowStart + 1].extend([0, 1, 1])
            newGrid[newRowStart + 2].extend([0, 0, 0])
        elif char == 'J':
            newGrid[newRowStart + 0].extend([0, 1, 0])
            newGrid[newRowStart + 1].extend([1, 1, 0])
            newGrid[newRowStart + 2].extend([0, 0, 0])
        elif char == '7':
            newGrid[newRowStart + 0].extend([0, 0, 0])
            newGrid[newRowStart + 1].extend([1, 1, 0])
            newGrid[newRowStart + 2].extend([0, 1, 0])
        elif char == 'F':
            newGrid[newRowStart + 0].extend([0, 0, 0])
            newGrid[newRowStart + 1].extend([0, 1, 1])
            newGrid[newRowStart + 2].extend([0, 1, 0])
        elif char == 'S':
            newGrid[newRowStart + 0].extend([1, 1, 1])
            newGrid[newRowStart + 1].extend([1, 1, 1])
            newGrid[newRowStart + 2].extend([1, 1, 1])
        else:
            newGrid[newRowStart + 0].extend([0, 0, 0])
            newGrid[newRowStart + 1].extend([0, 0, 0])
            newGrid[newRowStart + 2].extend([0, 0, 0])

# newGrid
# 0 : unsearched
# 1 : pipe
# 2 : searched

# bfs from 4 outer edges
rowsLen = len(newGrid)
colsLen = len(newGrid[0])
queue = []
# left & right columns
for row in range(rowsLen):
    queue.append((row, 0))
    queue.append((row, colsLen - 1))
# top & bottom rows
for col in range(1, colsLen - 1):
    queue.append((0, col))
    queue.append((colsLen - 1, col))

surroundings = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = set()
while len(queue) > 0:
    pos = queue.pop(0)
    if pos in visited:
        continue

    row, col = pos
    if row not in range(rowsLen) or col not in range(colsLen):
        continue

    char = newGrid[row][col]
    if char in [1, 2]:
        continue
    newGrid[row][col] = 2
    visited.add(pos)

    for rowDiff, colDiff in surroundings:
        newPos = (row + rowDiff, col + colDiff)
        queue.append(newPos)

# count 3x3 grids that do not contain a 2
res = 0
for rowStart in range(0, rowsLen, 3):
    for colStart in range(0, colsLen, 3):
        flag = True
        for rowDiff in range(3):
            for colDiff in range(3):
                if newGrid[rowStart + rowDiff][colStart + colDiff] == 2:
                    flag = False
        if flag:
            res += 1
            print((rowStart / 3, colStart / 3))
print(res - 1) # since also counts "S"