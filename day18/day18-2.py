# Like Part 1 but now the outer search has a list of four locations as
# the first element of its state.
# The results of inner searches for each quadrant are now cached instead
# of caching the entire outer transition results.

from collections import defaultdict
import astar
with open('input') as f:
    lines = [x.strip() for x in f]

Wall = set()
keys = dict() # map of key locations to lower case letters
doors = defaultdict(lambda:None) # map of lower case letters to door locations
y = 0
for line in lines:
    x = 0
    for c in line:
        if c == '#': Wall.add((x,y))
        if c == '@': start = (x,y)
        v = ord(c)
        if v in range(ord('a'), ord('z')+1):
            keys[(x,y)] = v # temp: hold letter in Key dict
        if v in range(ord('A'), ord('Z')+1):
            doors[v + ord('a') - ord('A')] = (x,y)
        x += 1
    y += 1

# Build map of key locations to corresponding door locations (if any)
Key = dict((k, doors[keys[k]]) for k in keys)

# Alter map for Part 2
x,y = start
for a,b in ((x,y),(x+1,y),(x-1,y),(x,y+1),(x,y-1)):
    Wall.add((a,b))

initial_locations = [(x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1)]

def trans(loc,keys): # Transition function for inner map search
    rv = []
    if loc in keys: return rv # If key found, don't go further
    x,y = loc
    for p in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if p not in Wall and p not in [Key[k] for k in keys]: rv.append((p,1))
    return rv

trans2cache = dict()
def trans2(state): # Transition function for outer key order search
    loctup, keys = state
    locs = list(loctup)
    if not keys:
        # No keys left: we're done!
        # Transition to the finished state with cost 0
        return [(True, 0)]
    rv = []
    for i in range(4):
        loc = locs[i]
        if (loc, keys) in trans2cache:
            reachable = trans2cache[(loc,keys)]
        else:
            a = astar.astar(loc,lambda x:trans(x,keys))
            srch = a.run(None)
            reachable = dict(s for s in srch if s[0] in keys)
            trans2cache[(loc,keys)] = reachable
        for k in reachable:
            newkeys = frozenset(keys - {k})
            newlocs = locs.copy()
            newlocs[i] = k
            rv.append(((tuple(newlocs), newkeys), reachable[k]))
    return rv

a = astar.astar((tuple(initial_locations), frozenset(Key.keys())), trans2)
sol = a.run(True) # Search for dummy end state
print(sol[0])
