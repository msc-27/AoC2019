from collections import defaultdict
import intcode
with open('input') as f:
    lines = [x.strip() for x in f]
csv = [x.split(',') for x in lines]
prog = [int(x) for x in csv[0]]
m = intcode.machine(prog)
m.run()

Map = defaultdict(int)
x=0; y=0
maxx = 0
v = m.get()
while v != None:
    if v == 10:
        x = -1 
        y += 1
    if v not in (10,46):
        Map[(x,y)] = 1
    x += 1
    maxx = max(maxx,x)
    v = m.get()
maxy = y

out = 0
for i in range(0,maxy):
    for j in range(0,maxx):
        if all([Map[(i,j)],Map[(i+1,j)],Map[(i-1,j)],Map[(i,j+1)],Map[(i,j-1)]]):
            out += i*j
print(out)
