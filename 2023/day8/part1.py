f = open("input.txt", "r")
#f = open("test.txt", "r")
#f = open("test2.txt", "r")
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

steps = 0
ptr = -1
pos = 'AAA'
while True:
    # base case
    if pos == 'ZZZ':
        break

    steps += 1
    ptr += 1
    if ptr == len(instruct):
        ptr = 0
    move = instruct[ptr]

    if move == 'L':
        pos = map[pos][0]
    elif move == 'R':
        pos = map[pos][1]

print(steps)

    