from collections import defaultdict
with open('input') as f:
    lines = [x.strip() for x in f]

bom = dict() # Bill of materials
for line in lines:
    srcs,targ = line.split('=>')
    tqs,to = targ.strip().split(' ')
    tq = int(tqs)
    srcl = []
    for src in srcs.split(','):
        sqs,so = src.strip().split(' ')
        sq = int(sqs)
        srcl.append((sq,so))
    bom[to] = (tq,srcl) # Base quantity, component list

req = [('FUEL',1)]
surplus = defaultdict(int)
ore_needed = 0

while req:
    chem, qty = req.pop(0)
    if chem == 'ORE':
        ore_needed += qty
        continue
    in_hand = min(qty, surplus[chem])
    surplus[chem] -= in_hand
    qty -= in_hand
    if qty == 0: continue
    bq, srcs = bom[chem]
    mult = qty / bq
    if mult != int(mult): mult += 1
    mult = int(mult)
    for src in srcs:
        req.append((src[1], mult * src[0]))
    surplus[chem] += bq * mult - qty

print(ore_needed)
