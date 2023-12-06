f = open("advent-of-code/2022/day1/input.txt", "r")
# f = open("advent-of-code/2022/day1/test.txt", "r")
lines = f.readlines()
lines.append('\n')

sum = 0
sums = []
for line in lines:
    line = line.split('\n')[0]
    if not line or line == '':
        sums.append(sum)
        sum = 0
    else:
        sum += int(line)
sums.sort(reverse=True)
print(sums[0] + sums[1] + sums[2])
