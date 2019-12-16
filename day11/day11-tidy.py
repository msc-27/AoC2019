from collections import defaultdict
import intcode
with open('input') as f:
    lines = [x.strip() for x in f]
csv = [x.split(',') for x in lines]
prog=[int(x) for x in csv[0]]

def do_turtle_artist(init):
    visited = defaultdict(int)
    visited[(0,0)] = init
    x = 0; y = 0; facing = 0
    turn = {0:(0,-1), 1:(1,0), 2:(0,1), 3:(-1,0)}
    m = intcode.machine(prog)
    while True:
        m.put(visited[(x,y)])
        m.run()
        if m.halted: break
        p = m.get()
        d = m.get()
        visited[(x,y)] = p
        if d == 0: facing = (facing + 3) % 4
        if d == 1: facing = (facing + 1) % 4
        x += turn[facing][0]
        y += turn[facing][1]
    return visited

v = do_turtle_artist(0)
print(len(v))

v = do_turtle_artist(1)
miny = min(x[1] for x in v)
maxy = max(x[1] for x in v)
minx = min(x[0] for x in v)
maxx = max(x[0] for x in v)
msg=''
for y in range(miny,maxy+1):
    for x in range(minx,maxx+1):
        msg += '*' if v[(x,y)] == 1 else ' '
    msg += '\n'
print(msg)
