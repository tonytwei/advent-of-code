f = open("local\input.txt", "r")
#f = open("local/test.txt", "r")

lines = f.readlines()
res = 0

map_map = {
    'seed-to-soil' : {},
    'soil-to-fertilizer' : {},
    'fertilizer-to-water' : {},
    'water-to-light' : {},
    'light-to-temperature' : {},
    'temperature-to-humidity' : {},
    'humidity-to-location' : {}
}
seeds = []
map_flag = ""
numLines = len(lines)
for idx, line in enumerate(lines):
    if "seeds" in line:
        seeds = line.split(':')[1].split()
        continue
    if "map" in line:
        map_flag = line.split()[0]
        continue
    if line == '\n':
        continue

    temp = line.split()
    dest = int(temp[0])
    src = int(temp[1])
    iter = int(temp[2])

    map_map[map_flag][src] = (dest, iter)


res = 99999999999
for seed in seeds:
    val = int(seed)
    
    for mapKey in map_map.keys():
        for src, value in map_map[mapKey].items():
            dest, iter = value

            keyDiff = val - src
            if keyDiff < 0 or keyDiff > iter:
                continue

            val = dest + keyDiff
            break

    print(val)
    res = min(res, val)
print(res)
