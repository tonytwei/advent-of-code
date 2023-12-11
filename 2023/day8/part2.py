f = open("2023\day8\input.txt", "r")
#f = open("2023/day8/test3.txt", "r")
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

numAPos = len(posToZ.keys())
from collections import defaultdict
seenNums = defaultdict(lambda: 0)

numbers = [tup[0] for tup in ZtoZ.values()]
print(numbers)

# need to find prime number factors for numbers
maxNumber = max(numbers)

# find the max possible prime 
from math import sqrt
searchRangeLen = int(sqrt(maxNumber))
print(searchRangeLen)

# search for possible primes
primes = set()
for i in range(searchRangeLen):
    if i == 1 or i == 0:
        continue
    isPrime = True
    for prime in primes:
        if i % prime != 0:
            isPrime = False
    if isPrime:
        primes.add(i)

from collections import defaultdict
factorCount = defaultdict(int)
for number in numbers:
    for factor in range(1, searchRangeLen):
        remainder = number % factor
        if remainder != 0:
            continue
        factorCount[prime] += 1
        factorCount[number / factor] += 1

numbersCount = len(numbers)
commonFactors = []
for factor, count in factorCount.items():
    if count == numbersCount:
        commonFactors.append(factor)

commonFactors.sort(reverse=True)
for factor in commonFactors:
    for i in range(len(numbers)):
        #number = numbers[i]
        numbers[i] /= factor

print(numbers)
res = 1
for number in numbers:
    res *= number
print(res)
for factor in commonFactors:
    res *= factor
print(res)

# 14299763833181
