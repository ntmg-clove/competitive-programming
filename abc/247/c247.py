import re
import sys
from pprint import pprint

sys.setrecursionlimit = 10 ** 6


PRINT_DEB = True
# PRINT_DEB = False


def debug_(msg: str, ppr: str = None) -> None:
    if not PRINT_DEB:
        return
    print(msg, end="")
    if ppr:
        pprint(ppr)
    else:
        print()

    return


S_1 = [1]


def rep(n: int):
    if n == 1:
        return S_1
    else:
        return rep(n - 1) + [n] + rep(n - 1)


N = int(input())

print(*rep(N))