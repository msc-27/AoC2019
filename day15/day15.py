import intcode
import astar
with open('input') as f:
    lines = [x.strip() for x in f]
csv = [x.split(',') for x in lines]
prog = [int(x) for x in csv[0]]
m = intcode.machine(prog)
maze = dict()

maze[(0,0)] = m # Install 'droid at starting location
target = None

def explore(p): # Find exits from location p
    global target # set this if the oxygen system is found
    move = {1:(0,1),2:(0,-1),3:(1,0),4:(-1,0)}
    rv = []
    x,y = p
    m = maze[(x,y)] # Get the 'droid installed at p
    for direction,reverse in zip([1,2,3,4],[2,1,4,3]):
        m.put(direction)
        m.run()
        r = m.get()
        if r in (1,2): # 'droid moved: add new location
            nx = x + move[direction][0]
            ny = y + move[direction][1]
            rv.append(((nx,ny),1))
            maze[(nx,ny)] = m.copy() # Clone the 'droid and leave it behind
            m.put(reverse) # Move the 'droid back whence it came
            m.run()
            _ = m.get()
            if r == 2:
                target = (nx,ny)
    return rv

import astar
a = astar.astar((0,0),explore)
states = a.run(None) # Explore fully and find target
print([s[1] for s in states if s[0] == target][0])

Map = [x[0] for x in states]
def trans(p): # Quicker transition function now we have the map
    rv = []
    x,y = p
    if (x,y+1) in Map: rv.append(((x,y+1),1))
    if (x,y-1) in Map: rv.append(((x,y-1),1))
    if (x+1,y) in Map: rv.append(((x+1,y),1))
    if (x-1,y) in Map: rv.append(((x-1,y),1))
    return rv

a = astar.astar(target,trans) # Part 2: target is now the initial state
solution = a.run(None) # Explore fully and get costs for all locations
print(max(x[1] for x in solution))
