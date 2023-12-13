f = open("input.txt", "r")
#f = open("test1.txt", "r")
#f = open("test2.txt", "r")
lines = f.readlines()
lines = [line.split('\n')[0] for line in lines]

# use split and count how many partitions .split(".")
def valid(string):
    global nums
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

# print(valid([3, 2, 1], ".###..#.##.#"))
# exit(0)
from functools import cache
@cache
def rec(resStr, buildStr, strPtr):
    global res
    if strPtr == len(resStr):
        if valid(buildStr):
            res += 1
        return
    
    resChar = resStr[strPtr]
    if resChar == ".":
        buildStr += "."
        strPtr += 1
        rec(resStr, buildStr, strPtr)
    elif resChar == "#":
        buildStr += "#"
        strPtr += 1
        rec(resStr, buildStr, strPtr)
    elif resChar == "?":
        strPtr += 1
        buildStrCopy = buildStr + '.'
        rec(resStr, buildStrCopy, strPtr)
        buildStrCopy = buildStr + '#'
        rec(resStr, buildStrCopy, strPtr)


res = 0
for index, line in enumerate(lines):
    resStr, resNums = line.split(" ")
    resNums = resNums.split(",")
    resNums = [int(num) for num in resNums]
    print((index, resStr, resNums))
    str = ""
    nums = []
    for i in range(5):
        str += resStr
        nums.extend(resNums)
    rec(str, "", 0) 
print(res)