import sys
from pprint import pprint
from collections import Counter

sys.setrecursionlimit = 10 ** 6


# PRINT_DEB = True
PRINT_DEB = False


def debug_(msg: str, ppr: str = None) -> None:
    if not PRINT_DEB:
        return
    print(msg, end="")
    if ppr:
        pprint(ppr)
    else:
        print()

    return


N, X, Y = map(int, input().split())

distance = Counter()
for i in range(N - 1):
    i += 1
    for j in range(i, N):
        j += 1

        key = min([j - i, abs(X - i) + abs(Y - j) + 1])
        # print(i, j, key)
        distance[key] += 1

for i in range(1, N):
    print(distance[i])
