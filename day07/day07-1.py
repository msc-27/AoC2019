import intcode
with open('input') as f:
    lines = [x.strip() for x in f]
csv = [x.split(',') for x in lines]

prog = [int(x) for x in csv[0]]
input_list = []
def inp():
    return input_list.pop(0)
def outp(x):
    input_list.insert(1,x)
outs = []

import itertools
for a,b,c,d,e in itertools.permutations([0,1,2,3,4]):
    input_list = [a,0,b,c,d,e]
    for x in range(5):
        m = intcode.machine(prog,inp,outp)
        m.run()
    outs.append(input_list[0])
print(max(outs))
