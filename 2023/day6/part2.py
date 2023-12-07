f = open("input.txt", "r")
#f = open("test.txt", "r")
lines = f.readlines()

times = lines[0].split(':')[1].split()
distances = lines[1].split(':')[1].split()
numRaces = len(times)

time = int(''.join(times))
distance = int(''.join(distances))

print(time)
print(distance)

waysToWin = 0
for timeHeld in range(1, time - 1):
    timeRemaining = time - timeHeld
    if timeHeld * timeRemaining > distance:
        waysToWin += 1
print((time, waysToWin))