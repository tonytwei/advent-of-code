f = open("2023/day9/input.txt", "r")
#f = open("2023/day9/test.txt", "r")
lines = f.readlines()

def solve(numbers):
    rows = []
    rows.append(numbers)
    allZeros = False
    while not allZeros:
        newRow = []
        allZeros = True
        for i in range(len(numbers) - 1):
            newNumber = numbers[i + 1] - numbers[i]
            if newNumber != 0:
                allZeros = False
            newRow.append(newNumber)
        numbers = newRow
        rows.append(newRow)
    print(rows)

    res = 0
    for row in rows:
        res += row[-1]
    return res

resSum = 0
for line in lines:
    numbers = line.split()
    numbers = [int(number) for number in numbers]
    resSum += solve(numbers)
print(resSum)