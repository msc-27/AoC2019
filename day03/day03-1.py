with open('input') as f:
    lines = [x.strip() for x in f]
csv = [x.split(',') for x in lines]

p1 = set()
p2 = set()

x,y = 0,0
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
        x += dx
        y += dy
        p1.add((x,y))
x,y = 0,0
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
        x += dx
        y += dy
        p2.add((x,y))

inters = p1 & p2
print(min(abs(p[0])+abs(p[1]) for p in inters))
