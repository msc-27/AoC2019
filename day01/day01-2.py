with open('input') as f:
    lines = [x.strip() for x in f]

t = 0
new = []
for x in [int(y) for y in lines]:
    f = x // 3 - 2
    t += f
    new += [f]
while new:
    new2 = []
    for x in new:
        f = x // 3 - 2
        if f > 0:
            t += f
            new2 += [f]
    new = new2
print(t)
