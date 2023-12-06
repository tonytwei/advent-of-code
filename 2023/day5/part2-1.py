#f = open("2023/day5/input.txt", "r")
f = open("2023/day5/test.txt", "r")
lines = f.readlines()

class customRange:
  def __init__(self, start, end):
    self.rangeStart = start
    self.rangeEnd = end

# parse seeds and maps
map_map = {}
mapKeys = []
mapKey = ""
for line in lines:
    if "seeds" in line:
        seedsRaw = line.split(':')[1].split()
        seedsRaw = [int(i) for i in seedsRaw]

        seedRanges = []
        for i in range(0, len(seedsRaw), 2):
            seedRanges.append(customRange(seedsRaw[i], seedsRaw[i] + seedsRaw[i + 1] - 1))
        continue
    
    if "map" in line:
        mapKey = line.split()[0]

        mapKeys.append(mapKey)
        map_map[mapKey] = {}
        map_map[mapKey]['src'] = []
        map_map[mapKey]['dest'] = []
        continue

    if line == '\n':
        continue
    
    splits = line.split()
    splits = [int(split) for split in splits]
    map_map[mapKey]['src'].append(customRange(splits[1], splits[1] + splits[2] - 1))
    map_map[mapKey]['dest'].append(customRange(splits[0], splits[0] + splits[2] - 1))

# append location range starting from 0
zeroFlag = False
minRangeStart = 99999999999
for srcRangeInterval in map_map['humidity-to-location']['src']:
    if srcRangeInterval.rangeStart == 0:
        zeroFlag = True
    minRangeStart = min(minRangeStart, srcRangeInterval.rangeStart)
if not zeroFlag:
    map_map['humidity-to-location']['src'].append(customRange(0, minRangeStart - 1))
    map_map['humidity-to-location']['dest'].append(customRange(0, minRangeStart - 1))

# sort seeds and map ranges
seedRanges.sort(key=lambda x: x.rangeStart)
for mapKey in mapKeys:
    map_map[mapKey]['zip'] = list(zip(map_map[mapKey]['src'], map_map[mapKey]['dest']))
    map_map[mapKey]['zip'].sort(key=lambda x: x[0].rangeStart)
    map_map[mapKey]['src'], map_map[mapKey]['dest'] = zip(*map_map[mapKey]['zip'])


# reverse ordering of mapKeys since we want to hash backwards
originalMapKeys = mapKeys
mapKeys.reverse()

def getValidRanges(range, mapDepth):
    # if at seed layer
    '''
    if mapDepth == len(mapKeys):
        print((range.rangeStart, range.rangeEnd))
        for seedRange in seedRanges:
            if not (seedRange.rangeStart <= range.rangeStart and range.rangeEnd <= seedRange.rangeEnd):
                continue
            return [range]
        return []
    '''
    if mapDepth == len(mapKeys):
        res = []
        start, end = range.rangeStart, range.rangeEnd
        for seedRange in seedRanges:
            if end < seedRange.rangeStart:
                continue
            if seedRange.rangeEnd < start:
                continue
            
            if start < seedRange.rangeStart:
                if end <= seedRange.rangeEnd:
                    res.append(customRange(seedRange.rangeStart, end))
                    start = end + 1
                    break
                elif seedRange.rangeEnd < end:
                    res.append(customRange(seedRange.rangeStart, seedRange.rangeEnd))
                    start = seedRange.rangeEnd + 1
                else:
                    print("ERROR #1")
            elif seedRange.rangeStart <= start:
                if end <= seedRange.rangeEnd:
                    res.append(customRange(start, end))
                    start = end + 1
                    break
                elif seedRange.rangeEnd < end:
                    res.append(customRange(start, seedRange.rangeEnd))
                    start = seedRange.rangeEnd + 1
                else:
                    print("ERROR #2")
        return res
    
    mapKey = mapKeys[mapDepth]
    
    srcRangeIntervals = []
    start, end = range.rangeStart, range.rangeEnd
    for mapRange in map_map[mapKey]['src']:
        if end < mapRange.rangeStart:
            continue
        if mapRange.rangeEnd < start:
            continue
        
        if start < mapRange.rangeStart:
            if end <= mapRange.rangeEnd:
                srcRangeIntervals.append(customRange(mapRange.rangeStart, end))
                start = end + 1
                break
            elif mapRange.rangeEnd < end:
                srcRangeIntervals.append(customRange(mapRange.rangeStart, mapRange.rangeEnd))
                start = mapRange.rangeEnd + 1
            else:
                print("ERROR #1")
        elif mapRange.rangeStart <= start:
            if end <= mapRange.rangeEnd:
                srcRangeIntervals.append(customRange(start, end))
                start = end + 1
                break
            elif mapRange.rangeEnd < end:
                srcRangeIntervals.append(customRange(start, mapRange.rangeEnd))
                start = mapRange.rangeEnd + 1
            else:
                print("ERROR #2")
    if start < end:
        srcRangeIntervals.append(customRange(start, end))
    print(("srcRangeIntervals", mapDepth, (range.rangeStart, range.rangeEnd), [(x.rangeStart, x.rangeEnd) for x in srcRangeIntervals]))

    destRangeIntervals = []
    for srcRangeInterval in srcRangeIntervals:
        hashDiff = ""
        for index, mapRange in enumerate(map_map[mapKey]['src']):
            if not (mapRange.rangeStart <= srcRangeInterval.rangeStart and srcRangeInterval.rangeEnd <= mapRange.rangeEnd):
                continue

            hashDiff = map_map[mapKey]['dest'][index].rangeStart - map_map[mapKey]['src'][index].rangeStart
            break
        if hashDiff == "":
            hashDiff = 0
        print(("hashDiff", hashDiff))
        newRange = customRange(srcRangeInterval.rangeStart + hashDiff, srcRangeInterval.rangeEnd + hashDiff)
        destRangeIntervals.append(newRange)
    print(("destRangeIntervals", mapDepth, (range.rangeStart, range.rangeEnd), [(x.rangeStart, x.rangeEnd) for x in destRangeIntervals]))
    
    validDestRangeIntervals = set()
    for destRangeInterval in destRangeIntervals:
        for validInterval in getValidRanges(destRangeInterval, mapDepth + 1):
            validDestRangeIntervals.add(validInterval)
    validDestRangeIntervals = list(validDestRangeIntervals)
    validDestRangeIntervals.sort(key=lambda x: x.rangeStart)
    print(("validDestRangeIntervals", mapDepth, (range.rangeStart, range.rangeEnd), [(x.rangeStart, x.rangeEnd) for x in validDestRangeIntervals]))

    if len(validDestRangeIntervals) == 0:
        return []

    validSrcRangeIntervals = []
    for validDestRangeinterval in validDestRangeIntervals:
        hashDiff = ""
        for index, mapRange in enumerate(map_map[mapKey]['dest']):
            if not (mapRange.rangeStart <= validDestRangeinterval.rangeStart and validDestRangeinterval.rangeEnd <= mapRange.rangeEnd):
                continue

            hashDiff = map_map[mapKey]['src'][index].rangeStart - map_map[mapKey]['dest'][index].rangeStart
            break
        if hashDiff == "":
            hashDiff = 0
        newRange = customRange(validDestRangeinterval.rangeStart + hashDiff, validDestRangeinterval.rangeEnd + hashDiff)
        validSrcRangeIntervals.append(newRange)
    print(("validSrcRangeIntervals", mapDepth, (range.rangeStart, range.rangeEnd), [(x.rangeStart, x.rangeEnd) for x in validSrcRangeIntervals]))

    print()
    return validSrcRangeIntervals

startMapKey = mapKeys[0]
validRanges = []
for startRange in map_map[startMapKey]['src']:
    validRanges.extend(getValidRanges(startRange, 0))

def valid(val):
    for mapKey in mapKeys:
        hashDiff = ""
        for index, mapRange in enumerate(map_map[mapKey]['src']):
            if not (mapRange.rangeStart <= val and val <= mapRange.rangeEnd):
                continue
            hashDiff = map_map[mapKey]['dest'][index].rangeStart - map_map[mapKey]['src'][index].rangeStart
            break
        if hashDiff == "":
            hashDiff = 0
        val += hashDiff

    # val = seed
    for seedRange in seedRanges:
        if seedRange.rangeStart <= val and val <= seedRange.rangeEnd:
            return True
    return False

rangeSum = 0
res = 9999999999
for validRange in validRanges:
    print(("validRange", (validRange.rangeStart, validRange.rangeEnd)))
    for i in range(validRange.rangeStart, validRange.rangeEnd + 1):
        if valid(i):
            res = min(res, i)
            #print(("answer:", res))
    rangeSum += validRange.rangeEnd - validRange.rangeStart
print(("res", res))

print((47, valid(47)))
print((46, valid(46)))
print((6, valid(6)))
# trying 1282710


# both valid ranges and def valid are wrong, bruhhh