from collections import defaultdict
import intcode
with open('input') as f:
    lines = [x.strip() for x in f]
csv = [x.split(',') for x in lines]
prog=[int(x) for x in csv[0]]

visited = defaultdict(int)
visited[(0,0)] = 0
x=0;y=0;facing=0
m = intcode.machine(prog)
while True:
    m.put(visited[(x,y)])
    m.run()
    if m.halted: break
    p = m.get()
    d = m.get()
    visited[(x,y)] = p
    if d == 0:
        facing -= 1
        if facing < 0: facing = 3
    if d == 1:
        facing += 1
        if facing > 3: facing = 0
    if facing == 0:
        y += 1
    if facing == 1:
        x += 1
    if facing == 2:
        y -= 1
    if facing == 3:
        x -= 1
print(len(visited))
