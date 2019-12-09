with open('input') as f:
    lines = [x.strip() for x in f]

orbs = [x.split(')') for x in lines]
counts = {}
def count(obj):
    if obj in counts: return counts[obj]
    rv = 0
    for orb in orbs:
        if orb[1] == obj:
            rv += 1
            rv += count(orb[0])
    counts[obj] = rv
    return rv
out = 0
for obj in [x[1] for x in orbs]:
    out += count(obj)
print(out)
