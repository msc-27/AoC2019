import intcode
with open('input') as f:
    lines = [x.strip('\n') for x in f]
csv = [x.split(',') for x in lines]
prog = [int(x) for x in csv[0]]

m = [intcode.machine(prog) for i in range(50)]
for i in range(50): m[i].put(i)

queue = [[] for i in range(50)]
sentto255 = None

while not sentto255:
    for i in range(50):
        m[i].run()
        addr = m[i].get()
        while addr != None:
            X = m[i].get()
            Y = m[i].get()
            if addr == 255 and sentto255 == None: sentto255 = Y
            if addr < 50: queue[addr].append((X,Y))
            addr = m[i].get()
        while queue[i]:
            instr = queue[i].pop(0)
            m[i].put(instr[0])
            m[i].put(instr[1])
        m[i].put(-1)
print(sentto255)
