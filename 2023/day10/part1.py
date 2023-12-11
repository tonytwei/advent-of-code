f = open("input.txt", "r")
#f = open("test1.txt", "r")
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

connections = {
    "|" : ["up", "down"],
    "-" : ["left", "right"],
    "L" : ["up", "right"],
    "J" : ["up", "left"],
    "7" : ["down", "left"],
    "F" : ["down", "right"]
}

oppositeDir = {
    "up" : "down",
    "down" : "up",
    "left" : "right",
    "right" : "left",
}

def validSearch(pos, searchDir):
    row, col = pos
    if row not in range(len(grid)) or col not in range(len(grid[0])):
        return False

    char = grid[row][col]
    if char in [".", "S"]:
        return False
    if oppositeDir[searchDir] in connections[char]:
        return True
    return False

def validDepth(pos, depth):
    row, col = pos
    if depthGrid[row][col] == -1:
        return True
    if depth < depthGrid[row][col]:
        return True
    return False

# grid = [[]]
surroundings = [(1, 0, "down"), (0, 1, "right"), (-1, 0, "up"), (0, -1, "left")]
searchList = [start]
maxDepth = 0
depth = 0
depthGrid = [[-1 for _ in grid[0]] for _ in grid]
while len(searchList) > 0:
    depth += 1
    searchListLen = len(searchList)
    for _ in range(searchListLen):
        curPos = searchList.pop(0)
        for surrounding in surroundings:
            searchPos = (curPos[0] + surrounding[0], curPos[1] + surrounding[1])
            #print((searchPos, surrounding[2], grid[searchPos[0]][searchPos[1]], valid(searchPos, surrounding[2])))
            if validSearch(searchPos, surrounding[2]) and validDepth(searchPos, depth):
                searchList.append(searchPos)
                depthGrid[searchPos[0]][searchPos[1]] = depth
                maxDepth = max(maxDepth, depth)
print(maxDepth)