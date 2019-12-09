with open('input') as f:
    masses = [int(x) for x in f]
total_1 = 0
total_2 = 0
for m in masses:
    f = m // 3 - 2
    total_1 += f
    while f > 0:
        total_2 += f
        f = f // 3 - 2

print(total_1)
print(total_2)
