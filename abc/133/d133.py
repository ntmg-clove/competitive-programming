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


N = int(input())
A = list(map(int, input().split()))

water = [0] * N

for i in range(N):
    water[i] = A[i] // 2 + A[i + 1 // N] // 2

print(*water)
