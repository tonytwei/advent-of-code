f = open("2023/day3/input.txt", "r")
#f = open("2023/day3/test.txt", "r")
text = [[char for char in line] for line in f]

gearLocations = {}
for row, line in enumerate(text):
    for col, char in enumerate(line):
        if char == '*':
            gearLocations[(row, col)] = []
        
def checkForGears(row, col):
    for rowDiff, colDiff in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]:
        newRow, newCol = row + rowDiff, col + colDiff
        if newRow not in range(len(text)) or newCol not in range(len(text[0])):
            continue
        if (newRow, newCol) in gearLocations:
            surroundingGears.add((newRow, newCol))

surroundingGears = set()
for row, line in enumerate(text):
    num = 0
    for col, char in enumerate(line):
        if char.isnumeric():
            num = num * 10 + int(char)
            checkForGears(row, col)
        else:
            for surroundingGear in surroundingGears:
                gearLocations[surroundingGear].append(num)
            surroundingGears.clear()
            num = 0

res = 0
for gearLocation, numArray in gearLocations.items():
    if len(numArray) == 2:
        res += numArray[0] * numArray[1]
print(res)