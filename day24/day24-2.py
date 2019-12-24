from collections import defaultdict
with open('input') as f:
    lines = [x.strip('\n') for x in f]

Map = defaultdict(lambda:'.')
for y,line in enumerate(lines):
    for x,c in enumerate(line):
        Map[(x,y)] = c

Maps = defaultdict(lambda:defaultdict(lambda:'.'))
Maps[0] = Map

def sumadj(lev,x,y):
    count = 0
    for p in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if Maps[lev][p] == '#': count += 1
    if (x,y) == (2,1):
        for x2 in range(5):
            if Maps[lev+1][(x2,0)] == '#': count += 1
    if (x,y) == (2,3):
        for x2 in range(5):
            if Maps[lev+1][(x2,4)] == '#': count += 1
    if (x,y) == (1,2):
        for y2 in range(5):
            if Maps[lev+1][(0,y2)] == '#': count += 1
    if (x,y) == (3,2):
        for y2 in range(5):
            if Maps[lev+1][(4,y2)] == '#': count += 1
    if y == 0:
        if Maps[lev-1][(2,1)] == '#': count += 1
    if y == 4:
        if Maps[lev-1][(2,3)] == '#': count += 1
    if x == 0:
        if Maps[lev-1][(1,2)] == '#': count += 1
    if x == 4:
        if Maps[lev-1][(3,2)] == '#': count += 1
    return count

for m in range(200):
    newmaps = defaultdict(lambda:defaultdict(lambda:'.'))
    for lev in range(-m-1,m+2):
        for y in range(5):
            for x in range(5):
                count = sumadj(lev,x,y)
                if Maps[lev][(x,y)] == '#':
                    if count == 1: newmaps[lev][(x,y)] = '#'
                else:
                    if count in (1,2): newmaps[lev][(x,y)] = '#'
        newmaps[lev][(2,2)] = '.'
    Maps = newmaps
out = sum(x == '#' for m in Maps.values() for x in m.values())
print(out)
