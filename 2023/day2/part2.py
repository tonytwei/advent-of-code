f = open("2023/day2/input.txt", "r")
#f = open("2023/day2/test.txt", "r")

import re

def solve(line):
    colourMin = {}
    
    game, rounds = line.split(":")

    for gameRounds in rounds.split(";"):
        for gameRound in gameRounds.split(","):
            gameRoundValues = gameRound.split()
            if gameRoundValues[1] not in colourMin:
                colourMin[gameRoundValues[1]] = int(gameRoundValues[0])
            elif int(gameRoundValues[0]) > colourMin[gameRoundValues[1]]:
                colourMin[gameRoundValues[1]] = int(gameRoundValues[0])

    res = 1
    for key, val in colourMin.items():
        res *= val
    return res

res = 0
for line in f:
    res += solve(line)
print(res)