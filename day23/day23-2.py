import intcode
with open('input') as f:
    lines = [x.strip('\n') for x in f]
csv = [x.split(',') for x in lines]
prog = [int(x) for x in csv[0]]

m = [intcode.machine(prog) for i in range(50)]
for i in range(50): m[i].put(i)

queue = [[] for i in range(50)]
idle = 0
toNAT = None
lastNAT = None

while True:
    idle += 1
    for i in range(50):
        m[i].run()
        addr = m[i].get()
        while addr != None:
            idle = 0
            X = m[i].get()
            Y = m[i].get()
            if addr == 255: toNAT = (X,Y)
            if addr < 50: queue[addr].append((X,Y))
            addr = m[i].get()
        while queue[i]:
            instr = queue[i].pop(0)
            m[i].put(instr[0])
            m[i].put(instr[1])
        m[i].put(-1)
    if idle == 3 and toNAT != None: # To be sure, wait for 3 idle loops
        if toNAT == lastNAT:
            print(toNAT[1])
            quit()
        lastNAT = toNAT
        m[0].put(toNAT[0])
        m[0].put(toNAT[1])
        idle = 0
