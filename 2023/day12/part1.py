f = open("input.txt", "r")
#f = open("test1.txt", "r")
#f = open("test2.txt", "r")
lines = f.readlines()
lines = [line.split('\n')[0] for line in lines]

# backtracking
'''
def rec(strSet, resStr, buildStr, resNums, strPtr, numPtr, numCount, canBeDamaged):
    return
    resChar = resStr[strPtr]
    print(resChar)
    if resChar == ".":
        buildStr += "."
        strPtr += 1
        canBeDamaged = True
        rec(strSet, resStr, buildStr, nums, strPtr, numPtr, numCount, canBeDamaged)
    elif resChar == "#":
        if not canBeDamaged:
            return
        numCount += 1
        if numCount == resNums[numPtr]:
            numPtr += 1
        canBeDamaged = False
        buildStr += "#"
        rec(strSet, resStr, buildStr, nums, strPtr, numPtr, numCount, canBeDamaged)
    elif resChar == "?":
        # 2 rec paths, we append "." or "#"
        return
'''

# use split and count how many partitions .split(".")
def valid(nums, string):
    '''
    numsPtr = 0
    canBeDamaged = True
    damagedCount = 0
    for index, char in enumerate(string):

        if numsPtr == len(nums):
            return False

        if char == ".":
            canBeDamaged = True
        elif char == "#":
            if not canBeDamaged:
                return False
            damagedCount += 1
            if damagedCount == nums[numsPtr]:
                damagedCount = 0
                numsPtr += 1
                canBeDamaged = False
    return numsPtr == len(nums)
    '''
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


def rec(resStr, resNums, buildStr, strPtr):
    global res
    if strPtr == len(resStr):
        if valid(resNums, buildStr):
            res += 1
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


res = 0
for line in lines:
    resStr, resNums = line.split(" ")
    resNums = resNums.split(",")
    resNums = [int(num) for num in resNums]
    #print((resStr, resNums))

    rec(resStr, resNums, "", 0) 
print(res)