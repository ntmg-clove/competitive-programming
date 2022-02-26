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

N, Q = map(int, input().split())
X = list(map(int, input().split()))

tree = [] * X
for _ in range(N - 1):
    A, B = map(int, input().split())
    
