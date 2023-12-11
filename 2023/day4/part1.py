f = open("adventOfCode2023/day4/input.txt", "r")
#f = open("adventOfCode2023/day4/test.txt", "r")

lines = f.readlines()

res = 0
for line in lines:
    winningNumsStr, ourNumsStr = line.split(':')[1].split('|')
    winningNums = set(winningNumsStr.split())
    ourNums = ourNumsStr.split()

    score = 0
    for ourNum in ourNums:
        if ourNum in winningNums:
            if score == 0:
                score = 1
            else:
                score *= 2
    res += score
print(res)
