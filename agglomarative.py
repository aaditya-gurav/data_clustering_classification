import math

dist = dict()
# list = [['p1',0.4,0.53], ['p2',0.22,0.38], ['p3',0.35,0.32], ['p4',0.26,0.19], ['p5',0.08,0.41], ['p6',0.45,0.30]]
list = [['p1',2,2], ['p2',3,2], ['p3',1,1], ['p4',3,1], ['p5',1.5,0.5]]
for i in list:
    for j in list:
        x = pow((i[1] - j[1]),2)
        y = pow((i[2] - j[2]),2)
        y = abs(y + x)
        dist[i[0],j[0]] = math.sqrt(y)

while len(dist) > 1:
    minimum = 100
    for i in dist:
        if(dist[i] > 0 and dist[i] <= minimum):
            minimum = dist[i]
            x = i
    for i in dist:
        if dist[(i[0],x[1])] < dist[(i[0],x[0])]:
            dist[(i[0],x[0])] = dist[(i[0],x[1])]
    for i in dist.copy():
        if(i[1] == x[1]):
            del dist[(i[0],x[1])]
    for i in dist.copy():
        if(i[0] == x[1]):
            del dist[(x[1],i[1])]
    for i in dist.copy():
        if i[1] == x[0]:
            dist[(i[0],(x))] = dist.pop(i)
    for i in dist.copy():
        if i[0] == x[0]:
            dist[((x),i[1])] = dist.pop(i)
    print(x)
    print("Minimum:", minimum)