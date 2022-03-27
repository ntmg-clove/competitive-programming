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

tmp = C[: N + 1]
idx = 0
start = tmp[0] // A[0]
addi = N + 1
while idx <= N + 1:
    debug_("---------------------------------")
    # print("idx", idx)
    # print("A", A)
    # print("B", B)
    # print("tmp", tmp)
    B.append(start)
    debug_("[start]:", start)
    tmp2 = []
    for i in range(N + 1):
        if i > 0:
            tmp2.append(tmp[i] - A[i] * start)
    if idx < N + 1:
        tmp2.append(C[addi])

    debug_("[tmp]", tmp)
    debug_("[tmp2]", tmp2)
    debug_("[B]", B)
    idx += 1
    addi += 1
    tmp = tmp2
    start = tmp[0] // A[0]

B.reverse()

print(*B)