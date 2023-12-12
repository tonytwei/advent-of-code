#f = open("input.txt", "r")
#f = open("test1.txt", "r")
f = open("test2.txt", "r")
lines = f.readlines()
lines = [line.split('\n')[0] for line in lines]

def valid(nums, string):
    #print(string)
    parts = string.split(".")
    newParts = []
    for i in range(len(parts)):
        if len(parts[i]) > 0:
            newParts.append(parts[i])

    #print(newParts)
    if len(newParts) != len(nums):
        return False


    for index, num in enumerate(nums):
        if num != len(newParts[index]):
            return False
        
    return True

# backtracking
def rec(resStr, resNums, buildStr, strPtr):
    global counts
    if strPtr == len(resStr):
        if valid(resNums, buildStr):
            start = buildStr[0]
            end = buildStr[-1]
            counts[(start, end)] += 1
        return
    
    resChar = resStr[strPtr]
    if resChar == ".":
        buildStr += "."
        strPtr += 1
        rec(resStr, resNums, buildStr, strPtr)
    elif resChar == "#":
        buildStr += "#"
        strPtr += 1
        rec(resStr, resNums, buildStr, strPtr)
    elif resChar == "?":
        strPtr += 1
        buildStrCopy = buildStr + '.'
        rec(resStr, resNums, buildStrCopy, strPtr)
        buildStrCopy = buildStr + '#'
        rec(resStr, resNums, buildStrCopy, strPtr)

def count(endedDot, depth):
    # index meanings
    # 0: ends in .
    # 1: ends in #
    if depth == MAX_SEARCH_DEPTH:
        return 1

    global counts
    ans = 0
    ans += counts[('.', '.')] * count(True, depth + 1)
    ans += counts[('.', '#')] * count(False, depth + 1)
    if endedDot:
        ans += counts[('#', '.')] * count(True, depth + 1)
        ans += counts[('#', '#')] * count(False, depth + 1)
    return ans

from collections import defaultdict
MAX_SEARCH_DEPTH = 4
res = 0
for line in lines:
    resStr, resNums = line.split(" ")
    resNums = resNums.split(",")
    resNums = [int(num) for num in resNums]
    print((resStr, resNums))

    counts = defaultdict(int)
    rec(resStr, resNums, "", 0)
    rec("." + resStr, resNums, "", 0)
    rec("#" + resStr, resNums, "", 0)
    
    count = count(True, 0)
    print(("count", count))
    res += count

print(("res", res))