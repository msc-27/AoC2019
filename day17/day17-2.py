from collections import defaultdict
import intcode
with open('input') as f:
    lines = [x.strip() for x in f]
csv = [x.split(',') for x in lines]
prog = [int(x) for x in csv[0]]
m = intcode.machine(prog)
m.poke(0,2)
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
    if chr(v) in ('^','v','<','>'):
        start = (x,y)
        direc = chr(v)
    x += 1
    maxx = max(maxx,x)
    v = m.get()
maxy = y

msg = ''
for y in range(maxy):
    for x in range(maxx):
        if (x,y) == start:
            msg += direc
        else:
            msg += '#' if Map[(x,y)] else '.'
    msg += '\n'
print(msg)

# Solved using pencil and paper from the above output

for c in 'A,B,A,C,B,A,C,B,A,C\n':
    m.put(ord(c))
for c in 'L,12,L,12,L,6,L,6\n':
    m.put(ord(c))
for c in 'R,8,R,4,L,12\n':
    m.put(ord(c))
for c in 'L,12,L,6,R,12,R,8\n':
    m.put(ord(c))
for c in 'n\n':
    m.put(ord(c))
m.run()
print(m._outputs[-1])
