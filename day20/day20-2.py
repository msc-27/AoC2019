from collections import defaultdict
import astar
with open('input') as f:
    lines = [x.strip('\n') for x in f]

Map = defaultdict(lambda:'#')
Portal = dict()

for y,line in enumerate(lines):
    for x,c in enumerate(line):
        Map[(x,y)] = c

width = max(len(line) for line in lines)
height = len(lines)
def islabel(s): return all('A' <= c <= 'Z' for c in s)

for y in range(height):
    for x in range(width):
        label = Map[(x,y)] + Map[(x+1,y)]
        if islabel(label):
            if Map[(x+2,y)] == '.': Portal[(x+2,y)] = label
            if Map[(x-1,y)] == '.': Portal[(x-1,y)] = label
        label = Map[(x,y)] + Map[(x,y+1)]
        if islabel(label):
            if Map[(x,y+2)] == '.': Portal[(x,y+2)] = label
            if Map[(x,y-1)] == '.': Portal[(x,y-1)] = label

Exits = defaultdict(list)
for loc in Portal:
    Exits[Portal[loc]].append(loc)

start = Exits['AA'][0]
end = Exits['ZZ'][0]

def trans(state):
    loc, level = state
    x,y = loc
    rv = []
    for d in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if Map[d] == '.': rv.append(((d,level),1))
    if loc in Portal:
        port = Portal[loc]
        if port not in ('AA','ZZ'):
            if x in (2, width-3) or y in (2, height-3):
                newlev = level - 1
            else:
                newlev = level + 1
            for exit in Exits[port]:
                if exit != loc and newlev >= 0:
                    rv.append(((exit,newlev),1))
    return rv

a = astar.astar((start,0),trans)
sol = a.run((end,0))
print(sol[0])
