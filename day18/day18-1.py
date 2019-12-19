# Answer originally found with very slow depth-first search on key order
# Faster approach: use nested BFS
# The outer search has states of the form (location, keys remaining)
# The target state is a dummy. It is available from any location when the 
# key list is empty and costs zero steps to reach.
# The outer transition function performs the inner search. Results are cached.
# The inner search is a usual map search, with states of the form (x,y).
# A full exploration is done in order to find all reachable remaining keys.
# The transition function takes the list of remaining keys as an extra
# parameter passed down from the outer search.

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

def trans(loc,keys): # Transition function for inner map search
    rv = []
    if loc in keys: return rv # If key found, don't go further on this path
    x,y = loc
    for p in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if p not in Wall and p not in [Key[k] for k in keys]: rv.append((p,1))
    return rv

trans2cache = dict()
def trans2(state): # Transition function for outer key order search
    if state in trans2cache: return trans2cache[state]
    loc, keys = state
    if not keys:
        # No keys left: we're done!
        # Transition to the finished state with cost 0
        return [(True, 0)]
    a = astar.astar(loc,lambda x:trans(x,keys))
    srch = a.run(None)
    reachable = dict(s for s in srch if s[0] in keys)
    rv = []
    for k in reachable:
        newkeys = frozenset(keys - {k})
        rv.append(((k, newkeys), reachable[k]))
    trans2cache[state] = rv
    return rv

a = astar.astar((start, frozenset(Key.keys())), trans2)
sol = a.run(True) # Search for dummy end state
print(sol[0])
