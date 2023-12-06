f = open("day1/input.txt", "r")
res = 0
for line in f:
    numbers = ''.join(c for c in line if c in '0123456789')
    res += 10 * int(numbers[0]) + int(numbers[-1])
print(res)