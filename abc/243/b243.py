import sys
from pprint import pprint
from collections import Counter, defaultdict

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


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

hits = []
blows = []

hit_flg = defaultdict(int)
a_contains = defaultdict(int)
b_contains = defaultdict(int)

for idx, (i, j) in enumerate(zip(A, B)):
    a_contains[i] = 1
    b_contains[j] = 1
    if i == j:
        hit_flg[idx] = 1
    else:
        hit_flg[idx] = 0

for i, j in enumerate(A):
    if not hit_flg[i] and b_contains[j]:
        blows.append(j)

debug_("", hit_flg)
debug_("", blows)

print(sum(hit_flg.values()))
print(len(blows))
