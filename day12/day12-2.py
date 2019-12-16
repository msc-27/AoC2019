import re
with open('input','r') as f:
    lines = [x.strip() for x in f]
moons_str = [re.findall('-?[0-9]+',x) for x in lines]

import itertools
repeat = []
# The three axes operate indepedently. Find repeating period for each one individually.
for axis in [0,1,2]:
    moons = [ [int(m[axis]),0] for m in moons_str ]
    seen = dict()
    seen[tuple((tuple(m) for m in moons))] = 0
    step = 0
    while True:
        m_new = [x.copy() for x in moons]
        for i,j in itertools.combinations([0,1,2,3],2):
            if moons[i][0] > moons[j][0]:
                m_new[i][1] -= 1
                m_new[j][1] += 1
            if moons[i][0] < moons[j][0]:
                m_new[i][1] += 1
                m_new[j][1] -= 1
        for m in m_new:
            m[0] += m[1]
        moons = m_new
        step += 1
        v = tuple((tuple(m) for m in moons))
        if v in seen: break
        seen[v] = step
    repeat.append((step,seen[v]))
print(repeat)

import fractions
if all(r[1] == 0 for r in repeat): # Easy case: true for puzzle input
    r1,r2,r3 = [r[0] for r in repeat]
    lcm1 = r1 * r2 // fractions.gcd(r1,r2)
    lcm = lcm1 * r3 // fractions.gcd(lcm1,r3)
    print(lcm)
