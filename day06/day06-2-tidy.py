from collections import defaultdict
import astar
with open('input') as f:
    lines = [x.strip() for x in f]
orbs = [x.split(')') for x in lines]

trans = defaultdict(list)
for a,b in orbs:
    trans[a].append((b,1))
    trans[b].append((a,1))

a = astar.astar('YOU',lambda x:trans[x])
sol = a.run('SAN')
print(sol[0]-2)
