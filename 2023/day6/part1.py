f = open("input.txt", "r")
#f = open("test.txt", "r")
lines = f.readlines()

times = lines[0].split(':')[1].split()
distances = lines[1].split(':')[1].split()
numRaces = len(times)

times = [int(time) for time in times]
distances = [int(distance) for distance in distances]
print(times)
print(distances)
# timeHeld * timeRemaining > distance

res = 1
for i in range(numRaces):
    waysToWin = 0
    time = times[i]
    distance = distances[i]
    for timeHeld in range(1, time - 1):
        timeRemaining = time - timeHeld
        if timeHeld * timeRemaining > distances[i]:
            waysToWin += 1
    res *= waysToWin
    print((time, waysToWin))
print(res)
#test ans: 288
#823680 incorrect answer