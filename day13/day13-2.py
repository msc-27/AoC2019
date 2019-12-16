import intcode
with open('input') as f:
    lines = [x.strip() for x in f]
csv = [x.split(',') for x in lines]
prog = [int(x) for x in csv[0]]
m = intcode.machine(prog)
m.poke(0,2)

pad = 0
bal = 0
score = 0
def process_output():
    global pad, bal, score
    x = m.get()
    y = m.get()
    z = m.get()
    while x != None:
        if x == -1: score = z
        if x != -1 and z == 3: pad = x
        if x != -1 and z == 4: bal = x
        x = m.get()
        y = m.get()
        z = m.get()

while not m.halted:
    m.run()
    process_output()
    if pad < bal: m.put(1)
    if pad == bal: m.put(0)
    if pad > bal: m.put(-1)
print(score)
