from collections import defaultdict
with open('input') as f:
    lines = [x.strip() for x in f]
csv = [x.split(',') for x in lines]

r = [int(x) for x in csv[0]]
r[1] = 12
r[2] = 2

pos = 0
while r[pos] != 99:
    op = r[pos]
    val1 = r[r[pos+1]]
    val2 = r[r[pos+2]]
    dest = r[pos+3]
    if op == 1: r[dest] = val1 + val2
    if op == 2: r[dest] = val1 * val2
    pos += 4
print(r[0])
