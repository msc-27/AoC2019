from collections import defaultdict
import intcode
with open('input') as f:
    lines = [x.strip() for x in f]
csv = [x.split(',') for x in lines]

prog = [int(x) for x in csv[0]]
inps = [[],[],[],[],[]]
def inp(x):
    return inps[x].pop(0)
collect = None
def wr_coll(x):
    global collect
    collect = x
outs = []

import itertools
for a,b,c,d,e in itertools.permutations([5,6,7,8,9]):
    m0 = intcode.machine(prog,lambda :inp(0), wr_coll)
    m1 = intcode.machine(prog,lambda :inp(1), wr_coll)
    m2 = intcode.machine(prog,lambda :inp(2), wr_coll)
    m3 = intcode.machine(prog,lambda :inp(3), wr_coll)
    m4 = intcode.machine(prog,lambda :inp(4), wr_coll)
    inps = [[a,0],[b],[c],[d],[e]]
    while not m4.halted:
        while not m0.halted and collect == None:
            m0.step()
        inps[1].append(collect)
        collect = None
        while not m1.halted and collect == None:
            m1.step()
        inps[2].append(collect)
        collect = None
        while not m2.halted and collect == None:
            m2.step()
        inps[3].append(collect)
        collect = None
        while not m3.halted and collect == None:
            m3.step()
        inps[4].append(collect)
        collect = None
        while not m4.halted and collect == None:
            m4.step()
        inps[0].append(collect)
        if collect != None: answ = collect
        collect = None
    outs.append(answ)
print(max(outs))
