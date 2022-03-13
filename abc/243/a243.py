import sys
from pprint import pprint

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


V, A, B, C = list(map(int, input().split()))


tmp = V
while True:
    tmp -= A
    if tmp < 0:
        print("F")
        break
    tmp -= B
    if tmp < 0:
        print("M")
        break
    tmp -= C
    if tmp < 0:
        print("T")
        break
