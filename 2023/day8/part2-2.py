f = open("2023\day8\input.txt", "r")
#f = open("2023/day8/test2-1.txt", "r")
lines = f.read()

instruct, mappings = lines.split('\n\n')

instruct = [char for char in instruct]

mappings = mappings.split('\n')
map = {}
for mapping in mappings:
    temp = mapping.split(' = ')
    src = temp[0]
    dest = temp[1]
    dest = dest.replace('(', '').replace(')', '').replace(',', '')
    left, right = dest.split()
    map[src] = (left, right)

positions = []
for src in map.keys():
    if src[2] == 'A':
        positions.append((src, src))

Zpositions = []
for src in map.keys():
    if src[2] == 'Z':
        Zpositions.append((src, src))
        #ZtoZ[src] = (0, src) # Zpos:(distToNextZ, nextZpos)

print(("positions", positions))
print(("Zpositions", Zpositions))


# distance of Zposition to next Z
ZtoZ = {}
steps = 0
ptr = -1
while True:
    steps += 1
    
    ptr += 1
    if ptr == len(instruct):
        ptr = 0
    move = instruct[ptr]
    moveIndex = ['L', 'R'].index(move)

    newZpositions = []
    for pos, src in Zpositions:
        nextPos = map[pos][moveIndex]
        if nextPos[2] == 'Z':
            ZtoZ[src] = (steps, nextPos)
        else:
            newZpositions.append((nextPos, src))
    Zpositions = newZpositions

    if len(Zpositions) == 0:
        break

print()
print(ZtoZ)
print(positions)
print()

posToZ = {}
steps = 0
ptr = -1
while True:
    steps += 1
    
    ptr += 1
    if ptr == len(instruct):
        ptr = 0
    move = instruct[ptr]
    moveIndex = ['L', 'R'].index(move)

    newPositions = []
    for pos, src in positions:
        nextPos = map[pos][moveIndex]
        if nextPos[2] == 'Z':
            posToZ[src] = (steps, nextPos)
        else:
            newPositions.append((nextPos, src))
    positions = newPositions

    if len(positions) == 0:
        break

print(("ZtoZ", ZtoZ))
print(("posToZ", posToZ))

numAPos = len(posToZ.keys())
from collections import defaultdict
seenNums = defaultdict(lambda: 0)
#print(numAPos)
'''
res = 0
mult = 0 # each element should have its own sum instead
flag = True
while flag:
    for src, temp in posToZ.items():
        distToZ, Zpos = temp
        #print((distToZ, Zpos))
        calcDist = distToZ + mult * ZtoZ[Zpos][0]

        seenNums[calcDist] += 1
        if seenNums[calcDist] == numAPos:
            flag = False
            res = calcDist
            break
    mult += 1
print(res)
'''
numbers = [tup[0] for tup in ZtoZ.values()]
# all numbers have a prime factor of 271 (found using google)
numbers = [number / 271 for number in numbers]
print(numbers)
res = 1
for number in numbers:
    res *= number
print(res * 271)

#14299763833181