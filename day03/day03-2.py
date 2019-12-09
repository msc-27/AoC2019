with open('input') as f:
    lines = [x.strip() for x in f]
csv = [x.split(',') for x in lines]

p1 = dict()
p2 = dict()

x,y = 0,0; steps=0
for inst in csv[0]:
    if inst[0] == 'U':
        dx=0;dy=1
    if inst[0] == 'D':
        dx=0;dy=-1
    if inst[0] == 'L':
        dx=-1;dy=0
    if inst[0] == 'R':
        dx=1;dy=0
    size = int(inst[1:])
    for i in range(size):
        steps += 1
        x += dx
        y += dy
        if (x,y) not in p1: p1[(x,y)] = steps
x,y = 0,0; steps=0
for inst in csv[1]:
    if inst[0] == 'U':
        dx=0;dy=1
    if inst[0] == 'D':
        dx=0;dy=-1
    if inst[0] == 'L':
        dx=-1;dy=0
    if inst[0] == 'R':
        dx=1;dy=0
    size = int(inst[1:])
    for i in range(size):
        steps += 1
        x += dx
        y += dy
        if (x,y) not in p2: p2[(x,y)] = steps

s1 = set(p1); s2 = set(p2)
inters = s1 & s2
print(min((p1[x] + p2[x] for x in inters)))
