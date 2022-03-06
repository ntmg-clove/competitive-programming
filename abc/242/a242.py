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


A, B, C, X = list(map(int, input().split()))

if X <= A:
    print(100 / 100)
elif X <= B:
    print(C / (B - A))
else:
    print(0)
