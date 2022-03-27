from audioop import add
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


N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

A.reverse()
C.reverse()

B = []

idx = 0
for i in range(M + 1):
    multi = C[i] // A[0]
    B.append(multi)
    for j in range(N + 1):
        C[i + j] = C[i + j] - multi * A[j]
    
    debug_("B:", B)
    debug_("C:", C)

B.reverse()

print(*B)