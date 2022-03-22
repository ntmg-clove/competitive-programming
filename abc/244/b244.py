import sys
from pprint import pprint

sys.setrecursionlimit = 10 ** 6


PRINT_DEB = True
# PRINT_DEB = False


def debug_(msg: str, ppr: str = None) -> None:
    if not PRINT_DEB:
        return
    print(msg)
    if ppr:
        pprint(ppr)

    return


N = int(input())
T = input()

now_point = [0, 0]
idx = 0
angles = ["E", "S", "W", "N"]

for t in T:
    if t == "R":
        idx += 1
        idx %= 4
    elif t == "S":
        if angles[idx] == "E":
            now_point = [now_point[0] + 1, now_point[1]]
        elif angles[idx] == "S":
            now_point = [now_point[0], now_point[1] - 1]
        elif angles[idx] == "W":
            now_point = [now_point[0] - 1, now_point[1]]
        elif angles[idx] == "N":
            now_point = [now_point[0], now_point[1] + 1]

print(*now_point)
