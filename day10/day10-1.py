with open('input') as f:
    lines = [x.strip() for x in f]

asts = set()
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == '#':
            asts.add((x,y))
best = 0
for ast in asts:
    angles_seen = set()
    for ast2 in asts - {ast}:
        dx,dy = (ast2[0]-ast[0], ast2[1]-ast[1])
        angle = None if dy == 0 else dx * 1000000 // dy
        side = (dy > 0) if dy != 0 else (dx > 0)
        angles_seen.add((angle,side))
    best = max(best, len(angles_seen))
print(best)
