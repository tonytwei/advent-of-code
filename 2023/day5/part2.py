f = open("2023/day5/input.txt", "r")
#f = open("2023/day5/test.txt", "r")
lines = f.readlines()

# parse seeds and maps
map_map = {
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
  def __init__(self, start, rangeLen):
    self.rangeStart = start
    self.rangeEnd = start + rangeLen - 1

# process input into hashmaps
map_flag = ""
for idx, line in enumerate(lines):
    if "seeds" in line:
        seedsRaw = line.split(':')[1].split()
        seedsRaw = [int(i) for i in seedsRaw]

        seeds = []
        for i in range(0, len(seedsRaw), 2):
            seeds.append(specialNumber(seedsRaw[i], seedsRaw[i + 1]))
        continue

    if "map" in line:
        map_flag = line.split()[0]
        continue

    if line == '\n':
        continue

    lineSplits = line.split()
    # flipped
    dest = specialNumber(int(lineSplits[1]), int(lineSplits[2]))
    src = specialNumber(int(lineSplits[0]), int(lineSplits[2]))

    map_map[map_flag][int(lineSplits[0])] = {'dest': dest, 'src': src}

# sort seeds
seeds = sorted(seeds, key=lambda seed: seed.rangeStart)

# reverse ordering of map iteration
mapKeys = list(map_map.keys())
mapKeys.reverse()

# inserting beginning layer if exists
# sorting layer maps keys
innerMapKeys = {}
for mapKey in mapKeys:
    if 0 not in map_map[mapKey]: map_map[mapKey][0] = {'dest': specialNumber(0, 1), 'src': specialNumber(0, 1)}
    innerMapKeys[mapKey] = list(map_map[mapKey].keys())
    # if 0 not in innerMapKeys[mapKey]: innerMapKeys[mapKey].insert(0, 0)
    innerMapKeys[mapKey].sort()

def hash(val, mapKey):
    for dest, src in map_map[mapKey].items():

        keyDiff = val - src
        if keyDiff < 0 or keyDiff > iter:
            continue

    return dest + keyDiff

def hashAllLayers(val):
    return 0

# specialNumber.rangeStart
# specialNumber.rangeEnd
# seeds / List[specialNumber]
# map_map / map[mapKey][int idx]: (specialNumber dest, specialNumber, src)
# mapKeys / List[mapKey]
# mapKey / String
# innerMapKeys[mapKeys] / List[int]
print(map_map['humidity-to-location'])
print()
tenMillion = 10000000

# actually location->humditity
for rangeStart in innerMapKeys['humidity-to-location']:
    print(rangeStart)
    print(map_map['humidity-to-location'][rangeStart]['src'].rangeStart)
    print(map_map['humidity-to-location'][rangeStart]['src'].rangeEnd)
    print()


# imagine water flowing into multiple streams