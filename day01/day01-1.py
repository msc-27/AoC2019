with open('input') as f:
    lines = [x.strip() for x in f]

t = 0
for x in [int(y) for y in lines]:
    t += x // 3 - 2
print(t)
