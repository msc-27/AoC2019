from collections import defaultdict
with open('input') as f:
    lines = [x.strip('\n') for x in f]

Map = defaultdict(lambda:'.')
for y,line in enumerate(lines):
    for x,c in enumerate(line):
        Map[(x,y)] = c

def key(m):
    return tuple((m[(x,y)] for y in range(5) for x in range(5)))

seen = set()
while key(Map) not in seen:
    seen.add(key(Map))
    newmap = defaultdict(lambda:'.')
    for y in range(5):
        for x in range(5):
            count = 0
            for p in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if Map[p] == '#': count += 1
            if Map[(x,y)] == '#':
                if count == 1:
                    newmap[(x,y)] = '#'
            else:
                if count in (1,2):
                    newmap[(x,y)] = '#'
    Map = newmap

out = 0
p = 1
for y in range(5):
    for x in range(5):
        if newmap[(x,y)] == '#': out += p
        p *= 2
print(out)
