with open('input') as f:
    lines = [x.strip() for x in f]

asts = set()
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == '#':
            asts.add((x,y))

def get_angle(dx,dy):
# Return angle in sortable (quadrant,gradient) integer format
# Avoid floats to avoid any equality comparison issues
    dy = -dy # Reverse y to match normal geometry
    scale = 1000000
    if dy == 0:
        angle = 0
        quad = 1 if dx > 0 else 3
    if (dx >= 0 and dy > 0):
        quad = 0
        angle = dx * scale // dy
    if (dx >  0 and dy < 0):
        quad = 1
        angle = -dy * scale // dx
    if (dx <= 0 and dy < 0):
        quad = 2
        angle = dx * scale // dy
    if (dx < 0 and dy > 0):
        quad = 3
        angle = -dy * scale // dx
    return (quad,angle)
    
def dist(a,b): return abs(a[0]-b[0]) + abs(a[1]-b[1])
def diff(a,b): return (a[0]-b[0], a[1]-b[1])

visible_count = []
for ast in asts:
    visible_set = {get_angle(*diff(ast2,ast)) for ast2 in asts - {ast}}
    visible_count.append((len(visible_set),ast))
visible_count.sort()
count, pos = visible_count[-1]
print(count, pos)

others = []
for ast in asts - {pos}:
    others.append((get_angle(*diff(ast,pos)), dist(ast,pos), ast))
others.sort() # Asteroids sorted by angle and distance from base

destroyed = 0
while others:
    angle = None
    temp = others.copy()
    for ast in temp:
        if ast[0] != angle:
            angle = ast[0]
            destroyed += 1
            print(destroyed,ast)
            others.remove(ast)
