import intcode
with open('input') as f:
    lines = [x.strip() for x in f]
csv = [x.split(',') for x in lines]
prog = [int(x) for x in csv[0]]

y = 100
left = 0
while True:
    x = left
    while True: # Find left edge of beam on row y
        m=intcode.machine(prog)
        m.put(x)
        m.put(y)
        m.run()
        v = m.get()
        if v: break
        x += 1
    left = x
    # Check if (x+99,y-99) is in the beam.
    # If so, then (x,y) is the bottom-left corner of the answer.
    m=intcode.machine(prog)
    m.put(x+99)
    m.put(y-99)
    m.run()
    v = m.get()
    if v: break
    y += 1

y -= 99
print(x*10000 + y)
