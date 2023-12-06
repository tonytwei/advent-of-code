#f = open("input.txt", "r")
f = open("test.txt", "r")
lines = f.readlines()

# parse seeds and maps
map_map = {
    'seed-to-seed': {},
    'seed-to-soil' : {},
    'soil-to-fertilizer' : {},
    'fertilizer-to-water' : {},
    'water-to-light' : {},
    'light-to-temperature' : {},
    'temperature-to-humidity' : {},
    'humidity-to-location' : {}
}

# treat ranges as individual units
class specialNumber:
  def __init__(self, start, end):
    self.rangeStart = start
    self.rangeEnd = end

# process input into hashmaps
map_flag = ""
for idx, line in enumerate(lines):
    if "seeds" in line:
        seedsRaw = line.split(':')[1].split()
        seedsRaw = [int(i) for i in seedsRaw]

        seeds = []
        for i in range(0, len(seedsRaw), 2):
            src = dest = specialNumber(seedsRaw[i], seedsRaw[i] + seedsRaw[i + 1] - 1)
            map_map['seed-to-seed'][seedsRaw[i]] = {'dest': dest, 'src': src}
        continue

    if "map" in line:
        map_flag = line.split()[0]
        continue

    if line == '\n':
        continue

    lineSplits = line.split()
    # flipped from part1
    src = specialNumber(int(lineSplits[1]), int(lineSplits[1]) + int(lineSplits[2]) - 1)
    dest = specialNumber(int(lineSplits[0]), int(lineSplits[0]) + int(lineSplits[2]) - 1)

    map_map[map_flag][int(lineSplits[1])] = {'dest': dest, 'src': src}

# sort seeds
seeds = sorted(seeds, key=lambda seed: seed.rangeStart)

# reverse ordering of map iteration
mapKeys = list(map_map.keys())
mapKeys.reverse()

# inserting beginning layer if exists
# sorting layer maps keys
innerMapKeys = {}
for mapKey in mapKeys:
    firstRangeLen = min(list(map_map[mapKey].keys()))
    if mapKey != 'seed-to-seed':
        if 0 not in map_map[mapKey]:
            map_map[mapKey][0] = {'dest': specialNumber(0, firstRangeLen - 1), 'src': specialNumber(0, firstRangeLen - 1)}
    innerMapKeys[mapKey] = list(map_map[mapKey].keys())
    innerMapKeys[mapKey].sort()


def hash(range, mapDepth):
    mapKey = mapKeys[mapDepth]
    #print((range.rangeStart, range.rangeEnd, mapDepth, mapKey))

    hashRangeStart = range.rangeStart
    hashRangeEnd = range.rangeEnd
    if range.rangeStart in map_map[mapKey]:
        hashRangeStart = map_map[mapKey][range.rangeStart]['dest'].rangeStart
        hashRangeEnd = map_map[mapKey][range.rangeStart]['dest'].rangeEnd

    return specialNumber(hashRangeStart, hashRangeEnd)

def unhash(range, mapDepth):
    mapKey = mapKeys[mapDepth]
    for rangeStartKey in innerMapKeys[mapKey]:
        rangeStart = map_map[mapKey][rangeStartKey]['dest'].rangeStart
        rangeEnd = map_map[mapKey][rangeStartKey]['dest'].rangeEnd

        hashDiff = map_map[mapKey][rangeStartKey]['src'].rangeStart - rangeStart

        if rangeStart <= range.rangeStart and range.rangeEnd <= rangeEnd:
            return specialNumber(range.rangeStart + hashDiff, range.rangeEnd + hashDiff)
    return range


def searchRange(srcRange, mapDepth):
    mapKey = mapKeys[mapDepth]
    #print((mapKey, "srcRange", srcRange.rangeStart, srcRange.rangeEnd))


    if mapKey == 'seed-to-seed':
        for rangeStart in innerMapKeys[mapKey]:
            rangeEnd = map_map[mapKey][rangeStart]['src'].rangeEnd

            withinRange = rangeStart <= srcRange.rangeStart and srcRange.rangeEnd <= rangeEnd
            if withinRange:
                return [srcRange]
        return []

    # grabbing srcIntervals that intersect with srcRange
    srcRangeIntervals = [] # type: List[specialNumber]
    lowerBound = srcRange.rangeStart
    upperBound = srcRange.rangeEnd
    for index, rangeStart in enumerate(innerMapKeys[mapKey]):
        rangeEnd = map_map[mapKey][rangeStart]['src'].rangeEnd
        # lowerBound, upperBound
        # rangeStart, rangeEnd
        if rangeEnd < lowerBound:
            continue
        if upperBound <= rangeStart:
            break

        if lowerBound < rangeStart:
            srcRangeIntervals.append(specialNumber(lowerBound, rangeStart))
        srcRangeIntervals.append(map_map[mapKey][rangeStart]['src'])
        lowerBound = rangeEnd + 1
    if mapKey != 'seed-to-seed' and lowerBound < upperBound:
        srcRangeIntervals.append(specialNumber(lowerBound, upperBound))

    

    destRangeIntervals = set()
    for srcRangeInterval in srcRangeIntervals:
        destRangeIntervals.add(hash(srcRangeInterval, mapDepth))
    destRangeIntervals = list(destRangeIntervals)
    destRangeIntervals.sort(key=lambda x: x.rangeStart)


    validDestRangeIntervals = set()
    for destRangeInterval in destRangeIntervals:
        temp = searchRange(destRangeInterval, mapDepth + 1)
        if len(temp) > 0:
            for range in temp:
                validDestRangeIntervals.add(range)
    validDestRangeIntervals = list(validDestRangeIntervals)
    validDestRangeIntervals.sort(key=lambda x: x.rangeStart)

    validSrcRangeIntervals = set()
    for validDestRangeInterval in validDestRangeIntervals:
        # write unhash
        validSrcRangeIntervals.add(unhash(validDestRangeInterval, mapDepth))
    validSrcRangeIntervals = list(validSrcRangeIntervals)
    validSrcRangeIntervals.sort(key=lambda x: x.rangeStart)
    return validSrcRangeIntervals

'''
map_map = {
    'seed-to-seed': {},
    'seed-to-soil' : {},
    'soil-to-fertilizer' : {},
    'fertilizer-to-water' : {},
    'water-to-light' : {},
    'light-to-temperature' : {},
    'temperature-to-humidity' : {},
    'humidity-to-location' : {}
}
'''
# actually location->humditity, flipped from part1
startMapKey = 'humidity-to-location'
validRanges = set()
validRangeStartInts = set()
for index, rangeStart in enumerate(innerMapKeys[startMapKey]):

    srcRange = map_map[startMapKey][rangeStart]['src']
    temp = searchRange(srcRange, 0)
    if len(temp) == 0:
        continue
    for range in temp:
        if range.rangeStart not in validRangeStartInts:
            validRanges.add(specialNumber(range.rangeStart, range.rangeEnd))
            validRangeStartInts.add(range.rangeStart)

validRanges = list(validRanges)
validRanges.sort(key=lambda x: x.rangeStart)

#print(validRanges)
sum = 0
for validRange in validRanges:
    print((validRange.rangeStart, validRange.rangeEnd))
    sum += validRange.rangeEnd - validRange.rangeStart
print(("sum", sum)) # 466462675

# specialNumber.rangeStart
# specialNumber.rangeEnd
# seeds / List[specialNumber]
# map_map / map[mapKey][int idx]: (specialNumber dest, specialNumber src)
# mapKeys / List[mapKey]
# mapKey / String
# innerMapKeys[mapKeys] / List[int]

def valid(val):
    for mapKey in mapKeys:
        for rangeStart in innerMapKeys[mapKey]:
            rangeEnd = map_map[mapKey][rangeStart]['src'].rangeEnd

            withinRange = rangeStart <= val and val < rangeEnd
            if withinRange:
                hashDiff = map_map[mapKey][rangeStart]['src'].rangeEnd - rangeStart
                val += hashDiff
                break
    return val

res = 99999999999999
for validRange in validRanges:
    a = validRange.rangeStart
    b = validRange.rangeEnd
    while a < b:
        if valid(a):
            if a < res:
                res = a
                print(res)
        a += 1
    #for i in range(a, b):
    #    if valid(i):
    #        print("yes")
# 149377034 incorrect