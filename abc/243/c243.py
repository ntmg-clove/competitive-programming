import sys
from pprint import pprint
from collections import defaultdict

sys.setrecursionlimit = 10 ** 6


# PRINT_DEB = True
PRINT_DEB = False


def debug_(msg: str, ppr: str = None) -> None:
    if not PRINT_DEB:
        return
    print(msg)
    if ppr:
        pprint(ppr)

    return


collision = False
points = defaultdict(lambda: {"R": None, "L": None})

N = int(input())
x_y = []
for _ in range(N):
    X, Y = map(int, input().split())
    x_y.append([X, Y])
S = input()

for xy, rl in zip(x_y, S):
    x, y = xy
    debug_([xy, rl])

    if rl == "R":
        if points[y][rl] is None:
            points[y][rl] = x
        else:
            if x < points[y][rl]:
                points[y][rl] = x

    elif rl == "L":
        if points[y][rl] is None:
            points[y][rl] = x
        else:
            if x > points[y][rl]:
                points[y][rl] = x

for elem in points.values():
    if elem["R"] is not None and elem["L"] is not None:
        if elem["R"] < elem["L"]:
            collision = True

debug_("points:", points)

if collision:
    print("Yes")
else:
    print("No")
