f = open("day1/input.txt", "r")

numberWords = ['zero', "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

res = 0
for line in f:
    firstNum = -1
    for i in range(len(line)):
        if line[i] in numbers:
            firstNum = int(line[i])
        for index, word in enumerate(numberWords):
            if word in line[:i]:
                firstNum = int(index)
        if firstNum != -1: break

    lastNum = -1
    for i in range(len(line) - 1, -1, -1):
        if line[i] in numbers:
            lastNum = int(line[i])
        for index, word in enumerate(numberWords):
            if word in line[i:]:
                lastNum = int(index)
        if lastNum != -1: break

    calc = firstNum * 10 + lastNum
    res += calc
print(res)