import re
with open('input','r') as f:
    lines = [x.strip() for x in f]
moons_str = [re.findall('-?[0-9]+',x) for x in lines]
moons = [[int(x) for x in m] + [0,0,0] for m in moons_str]

import itertools
for x in range(1000):
    m_new = [x.copy() for x in moons]
    for i,j in itertools.combinations([0,1,2,3],2):
        if moons[i][0] > moons[j][0]:
            m_new[i][3] -= 1
            m_new[j][3] += 1
        if moons[i][0] < moons[j][0]:
            m_new[i][3] += 1
            m_new[j][3] -= 1
        if moons[i][1] > moons[j][1]:
            m_new[i][4] -= 1
            m_new[j][4] += 1
        if moons[i][1] < moons[j][1]:
            m_new[i][4] += 1
            m_new[j][4] -= 1
        if moons[i][2] > moons[j][2]:
            m_new[i][5] -= 1
            m_new[j][5] += 1
        if moons[i][2] < moons[j][2]:
            m_new[i][5] += 1
            m_new[j][5] -= 1
    for m in m_new:
        m[0] += m[3]
        m[1] += m[4]
        m[2] += m[5]
    moons = m_new

out = 0
for m in moons:
    pe = abs(m[0]) + abs(m[1]) + abs(m[2])
    ke = abs(m[3]) + abs(m[4]) + abs(m[5])
    out += pe * ke
print(out)
