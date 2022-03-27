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


A, B, C, D = list(map(int, input().split()))

if A < C:
    print("Takahashi")
elif A > C:
    print("Aoki")
else:
    if B < D:
        print("Takahashi")
    elif B > D:
        print("Aoki")
    else:
        print("Takahashi")
