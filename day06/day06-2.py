import astar
with open('input') as f:
    lines = [x.strip() for x in f]
orbs = [x.split(')') for x in lines]

def trans(obj):
    rv = []
    for orb in orbs:
        if orb[1] == obj:
            rv.append((orb[0], 1))
        if orb[0] == obj:
            rv.append((orb[1], 1))
    return rv

a = astar.astar('YOU',trans)
sol = a.run('SAN')
print(sol[0]-2)
