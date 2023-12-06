f = open("advent-of-code/2022/day1/input.txt", "r")
lines = f.readlines()

res = 0
count = 0
for line in lines:
    line = line.split('\n')[0]
    if line == '':
        res = max(res, count)
        count = 0
    else:
        count += int(line)
print(res)