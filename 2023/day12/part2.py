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
    global a
    global b
    if strPtr == len(resStr):
        if valid(resNums, buildStr):
            end = buildStr[-1]
            if end == '.':
                a += 1
            elif end == '#':
                b += 1
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

def count(startCounts, dotCounts, hashCounts, endedDot, depth):
    # index meanings
    # 0: ends in .
    # 1: ends in #
    ans = 0
    if depth == 0:
        ans += startCounts[0] * count(startCounts, dotCounts, hashCounts, True, depth + 1)
        ans += startCounts[1] * count(startCounts, dotCounts, hashCounts, False, depth + 1)
        return ans
    elif depth == MAX_SEARCH_DEPTH:
        return 1

    ans += dotCounts[0] * count(startCounts, dotCounts, hashCounts, True, depth + 1)
    ans += dotCounts[1] * count(startCounts, dotCounts, hashCounts, False, depth + 1)
    if endedDot:
        ans += hashCounts[0] * count(startCounts, dotCounts, hashCounts, True, depth + 1)
        ans += hashCounts[1] * count(startCounts, dotCounts, hashCounts, False, depth + 1)
    return ans

MAX_SEARCH_DEPTH = 2
res = 0
for line in lines:
    resStr, resNums = line.split(" ")
    resNums = resNums.split(",")
    resNums = [int(num) for num in resNums]
    print((resStr, resNums))

    a = b = 0
    rec(resStr, resNums, "", 0)
    startCounts = (a, b)

    a = b = 0
    rec("." + resStr, resNums, "", 0)
    dotCounts = (a, b)

    a = b = 0
    rec("#" + resStr, resNums, "", 0)
    hashCounts = (a, b)

    print(startCounts)
    print(dotCounts)
    print(hashCounts)

    
    count = count(startCounts, dotCounts, hashCounts, True, 0)
    print(("count", count))
    res += count

print(("res", res))