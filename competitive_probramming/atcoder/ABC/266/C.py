# BD>BA, BD>BC, CA>BC, CA>CD, DB>DC, DB>DA, AC>AD, AC>AB

import math

Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Dx, Dy = map(int, input().split())

def distance(x1, x2, y1, y2):
    return math.sqrt((x1-y1)**2 + (x2-y2)**2)

if distance(Bx, By, Dx, Dy) > distance(Ax, Ay, Bx, By) and \
    distance(Bx, By, Dx, Dy) > distance(Bx, By, Cx, Cy) and \
    distance(Cx, Cy, Ax, Ay) > distance(Bx, By, Cx, Cy) and \
    distance(Cx, Cy, Ax, Ay) > distance(Cx, Cy, Dx, Dy) and \
    distance(Dx, Dy, Bx, By) > distance(Dx, Dy, Cx, Cy) and \
    distance(Dx, Dy, Bx, By) > distance(Dx, Dy, Ax, Ay) and \
    distance(Ax, Ay, Cx, Cy) > distance(Ax, Ay, Dx, Dy) and \
    distance(Ax, Ay, Cx, Cy) > distance(Ax, Ay, Bx, By):
    print("Yes")
else:
    print("No")