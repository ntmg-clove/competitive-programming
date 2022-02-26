from collections import defaultdict
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


N, M = map(int, input().split())
A = list(map(int, input().split()))
stocks = defaultdict(int)
for i in A:
    stocks[i] += 1

a_flg = [False] * N
B = list(map(int, input().split()))

flg = True
for i in B:
    if stocks[i]:
        stocks[i] -= 1
    else:
        flg = False
        break

if flg:
    print("Yes")
else:
    print("No")
