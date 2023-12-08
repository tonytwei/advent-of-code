f = open("input.txt", "r")
#f = open("test2-1.txt", "r")
lines = f.read()

instruct, mappings = lines.split('\n\n')

instruct  = [char for char in instruct]

mappings = mappings.split('\n')
map = {}
for mapping in mappings:
    temp = mapping.split(' = ')
    src = temp[0]
    dest = temp[1]
    dest = dest.replace('(', '').replace(')', '').replace(',', '')
    left, right = dest.split()
    map[src] = (left, right)
#print(map)

positions = []
for src in map.keys():
    if src[2] == 'A':
        positions.append(src)

Zpositions = []
ZcycleLen = {}
for src in map.keys():
    if src[2] == 'Z':
        Zpositions.append(src)
        ZcycleLen[src] = 0

# distance of Zposition -> Zpositino
steps = 0
ptr = -1
while True:
    steps += 1

    ptr += 1
    if ptr == len(instruct):
        ptr = 0
    move = instruct[ptr]
    moveIndex = ['L', 'R'].index(move)

    newZPositions = []
    for pos in Zpositions:
        newZPositions.append(map[pos][moveIndex])
    Zpositions = newZPositions

    newZPositions = []
    for pos in Zpositions:
        if pos[2] == 'Z':
            ZcycleLen[pos] = steps
        else:
            newZPositions.append(pos)
    Zpositions = newZPositions

    # if all positions have last char of 'Z'
    if len(Zpositions) == 0:
        break



posToZLen = {}

newPositions = []
for pos in positions:
    newPositions.append((pos, pos))
positions = newPositions


steps = -1
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
        if pos[2] == 'Z':
            posToZLen[src] = (steps, pos)
        else:
            newPositions.append((map[pos][moveIndex], src))
    positions = newPositions

    if len(positions) == 0:
        break



print(ZcycleLen)
print(posToZLen)
numAPos = len(posToZLen.keys())
from collections import defaultdict
seenNums = defaultdict(int)
print(numAPos)
mult = 0
flag = True
res = 0
while flag:
    for distToZ, endPos in posToZLen.values():
        totDist = distToZ + mult * ZcycleLen[endPos]
        #print((distToZ, endPos))
        #print(totDist)
        seenNums[totDist] += 1
        if seenNums[totDist] == numAPos:
            flag = False
            res = totDist
    
    mult += 1
            
print(res)
# 19783 wrong
