f = open("input.txt", "r")
#f = open("test.txt", "r")
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

# sort seeds and map ranges
seedRanges.sort(key=lambda x: x.rangeStart)
for mapKey in mapKeys:
    map_map[mapKey]['src'].sort(key=lambda x: x.rangeStart)
    map_map[mapKey]['dest'].sort(key=lambda x: x.rangeStart)

# reverse ordering of mapKeys since we want to hash backwards
mapKeys.reverse()


def getValidRanges(range, mapDepth):
    mapKey = mapKeys[mapDepth]
    
    srcRangeIntervals = []
    for mapRange in map_map[mapKey]['src']:
        if range.rangeEnd < mapRange.rangeStart:
            continue
        if mapRange.rangeEnd < range.rangeStart:
            continue
        srcRangeIntervals.append(mapRange)
    print(("srcRangeIntervals", (range.rangeStart, range.rangeEnd), [(x.rangeStart, x.rangeEnd) for x in srcRangeIntervals]))

    destRangeIntervals = []
    for srcRangeInterval in srcRangeIntervals:
        for index, mapRange in enumerate(map_map[mapKey]['src']):
            if srcRangeInterval.rangeStart != mapRange.rangeStart:
                continue
            hashDiff = map_map[mapKey]['src'][index].rangeStart - map_map[mapKey]['dest'][index].rangeStart
            newRange = customRange(srcRangeInterval.rangeStart + hashDiff, srcRangeInterval.rangeEnd + hashDiff)
            destRangeIntervals.append(newRange)
    print(("destRangeIntervals", (range.rangeStart, range.rangeEnd), [(x.rangeStart, x.rangeEnd) for x in destRangeIntervals]))
    
    
    print()
    return []

startMapKey = mapKeys[0]
validRanges = []
for startRange in map_map[startMapKey]['src']:
    validRanges.extend(getValidRanges(startRange, 0))