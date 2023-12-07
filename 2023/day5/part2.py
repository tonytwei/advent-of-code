f = open("input.txt", "r")
#f = open("test.txt", "r")
lines = f.read()

mapBlocks = lines.split('\n\n')

rawSeeds = mapBlocks.pop(0)
rawSeeds = rawSeeds.split(':')[1].split()
rawSeeds = [int(rawSeed) for rawSeed in rawSeeds]
seeds = []
for i in range(0, len(rawSeeds), 2):
    seeds.append((rawSeeds[i], rawSeeds[i] + rawSeeds[i + 1]))

for index, mapIntervals in enumerate(mapBlocks):
    rawIntervals = mapIntervals.split(':\n')[1].split()
    intervals = []
    for i in range(0, len(rawIntervals), 3):
        destStart, srcStart, rangeLen = [int(x) for x in rawIntervals[i:i+3]]

        # (intervalStart, intervalEnd, diff)
        interval = (srcStart, srcStart + rangeLen, destStart - srcStart)
        intervals.append(interval)
    
    newSeeds = []
    while len(seeds) > 0:
        seed = seeds.pop()
        seedStart, seedEnd = seed[0], seed[1]

        seedProcessed = False
        for intervalStart, intervalEnd, diff in intervals:
            if seedStart < intervalStart:
                if seedEnd <= intervalStart:
                    continue
                elif intervalStart < seedEnd and seedEnd <= intervalEnd:
                    seeds.append((seedStart, intervalStart))
                    newSeeds.append((intervalStart + diff, seedEnd + diff))
                    seedProcessed = True
                elif intervalEnd < seedEnd:
                    seeds.append((seedStart, intervalStart))
                    newSeeds.append((intervalStart + diff, intervalEnd + diff))
                    seeds.append((intervalEnd, seedEnd))
                    seedProcessed = True
                else:
                    print("INTERVAL ERROR")
            elif intervalStart <= seedStart and seedStart < intervalEnd:
                if seedEnd <= intervalEnd:
                    newSeeds.append((seedStart + diff, seedEnd + diff))
                    seedProcessed = True
                elif intervalEnd < seedEnd:
                    newSeeds.append((seedStart + diff, intervalEnd + diff))
                    seeds.append((intervalEnd, seedEnd))
                    seedProcessed = True
                else:
                    print("INTERVAL ERROR")
            elif intervalEnd <= seedStart:
                continue
            else:
                print("INTERVAL ERROR")
        if not seedProcessed:
            newSeeds.append((seedStart, seedEnd))
    seeds = newSeeds

seeds.sort(key=lambda x: x[0])
print(seeds[0][0])
