import re
f = open("2023/day2/input.txt", "r")

colourMax = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def solve(line):
    game, rounds = line.split(":")
    gameID = int(re.search(r"Game ([0-9]+)", game).group(1))

    for gameRounds in rounds.split(";"):
        for gameRound in gameRounds.split(","):
            gameRoundValues = gameRound.split()
            if colourMax[gameRoundValues[1]] < int(gameRoundValues[0]):
                return 0

    return gameID

res = 0
for line in f:
    res += solve(line)
print(res)