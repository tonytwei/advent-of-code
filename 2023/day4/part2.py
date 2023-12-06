f = open("adventOfCode2023/day4/input.txt", "r")
#f = open("adventOfCode2023/day4/test.txt", "r")

lines = f.readlines()
linesCount = len(lines)

from collections import defaultdict
multiplier = defaultdict(lambda: 1)

res = 0
for count, line in enumerate(lines):
    winningNumsStr, ourNumsStr = line.split(':')[1].split('|')
    winningNums = set(winningNumsStr.split())
    ourNums = ourNumsStr.split()

    score = 0
    for ourNum in ourNums:
        if ourNum in winningNums:
            score += 1

    for i in range(1, score + 1):
        multiplier[count + i] += multiplier[count]
    res += multiplier[count]
print(res)
