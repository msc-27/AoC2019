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
    if len(angles_seen) > best:
        best = len(angles_seen)
        best_loc = ast

dest=dict()
for ast in asts - {best_loc}:
    dx,dy = (ast[0]-best_loc[0], -(ast[1]-best_loc[1])) # Note y inversion
    angle = None if dy == 0 else dx * 1000000 // dy
    side = (dy > 0) if dy != 0 else (dx > 0)
    dest[ast] = (angle,side)

def dist(a): return abs(a[0]-best_loc[0]) + abs(a[1]-best_loc[1])
destroyed = 0
# Barely readable quadrant-by-quadrant search code
# It's what I scrabbled together quickly on the day
while dest:
    q = [a for a in dest if dest[a][0] != None and dest[a][0] >= 0 and dest[a][1] == True]
    q.sort(key=lambda x:(dest[x],dist(x)))
    ang = None
    for a in q:
        if dest[a][0] != ang:
            ang = dest[a][0]
            destroyed += 1
            print(destroyed,a,dest[a])
            del dest[a]
    horiz = [a for a in dest if dest[a][0] == None and dest[a][1] == True]
    if horiz:
        horiz.sort(key=lambda x:dist(x))
        destroyed += 1
        print(destroyed,horiz[0],dest[horiz[0]])
        del dest[horiz[0]]
    q = [a for a in dest if dest[a][0] != None and dest[a][0] < 0 and dest[a][1] == False]
    q.sort(key=lambda x:(dest[x],dist(x)))
    ang = None
    for a in q:
        if dest[a][0] != ang:
            ang = dest[a][0]
            destroyed += 1
            print(destroyed,a,dest[a])
            del dest[a]
    q = [a for a in dest if dest[a][0] != None and dest[a][0] >= 0 and dest[a][1] == False]
    q.sort(key=lambda x:(dest[x],dist(x)))
    ang = None
    for a in q:
        if dest[a][0] != ang:
            ang = dest[a][0]
            destroyed += 1
            print(destroyed,a,dest[a])
            del dest[a]
    horiz = [a for a in dest if dest[a][0] == None and dest[a][1] == False]
    if horiz:
        horiz.sort(key=lambda x:dist(x))
        destroyed += 1
        print(destroyed,horiz[0],dest[horiz[0]])
        del dest[horiz[0]]
    q = [a for a in dest if dest[a][0] != None and dest[a][0] < 0 and dest[a][1] == True]
    q.sort(key=lambda x:(dest[x],dist(x)))
    ang = None
    for a in q:
        if dest[a][0] != ang:
            ang = dest[a][0]
            destroyed += 1
            print(destroyed,a,dest[a])
            del dest[a]
