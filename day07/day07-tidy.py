import intcode_new as intcode
with open('input') as f:
    lines = [x.strip() for x in f]
csv = [x.split(',') for x in lines]

prog = [int(x) for x in csv[0]]
outs = []

import itertools
for perm in itertools.permutations([0,1,2,3,4]):
    val = 0
    for x in perm:
        m = intcode.machine(prog)
        m.put(x)
        m.put(val)
        m.run()
        val = m.get()
    outs.append(val)
print(max(outs))

outs = []
for perm in itertools.permutations([5,6,7,8,9]):
    amps = [intcode.machine(prog) for x in range(5)]
    for amp,inp in zip(amps,perm): amp.put(inp)
    amps[0].put(0)
    while not all(x.halted for x in amps):
        for amp in amps: amp.run()
        for a,b in zip(amps, amps[1:] + amps[0:1]):
            v = a.get()
            while v != None:
                b.put(v)
                result = v
                v = a.get()
    outs.append(result)
print(max(outs))
