f = open("2023/day3/input.txt", "r")
#f = open("2023/day3/test.txt", "r")

text = [[char for char in line] for line in f]

def checkValid(row, col):
    for rowDiff, colDiff in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]:
        newRow, newCol = row + rowDiff, col + colDiff
        if newRow not in range(len(text)) or newCol not in range(len(text[0])):
            continue
        char = text[newRow][newCol]
        if not char.isnumeric() and char != '.' and char != '\n':
            return True
    return False

res = 0
for row, line in enumerate(text):
    num = 0
    numValid = False
    for col, char in enumerate(line):
        if char.isnumeric():
            if not numValid:
                numValid = checkValid(row,col)
            num = num * 10 + int(char)
        else:
            if numValid:
                res += num
                num = 0
                numValid = False
            else:
                num = 0
print(res)