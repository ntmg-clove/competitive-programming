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

numlist = [_ for _ in range(1, 2 * N + 2)]
flgs = [False] * (2 * N + 1)
pointa = 0

while True:
    while flgs[pointa]:
        pointa += 1

    flgs[pointa] = True
    print(numlist[pointa])

    s = int(input())
    if s == 0:
        break

    flgs[s - 1] = True
