from itertools import count
import sys
from pprint import pprint
from collections import defaultdict

sys.setrecursionlimit = 10 ** 6


# PRINT_DEB = True
PRINT_DEB = False


def debug_(msg: str, ppr: str = None) -> None:
    if not PRINT_DEB:
        return
    print(msg, end="")
    if ppr:
        pprint(ppr)
    else:
        print()

    return


N, M = map(int, input().split())

dd = defaultdict(list)

for i in range(M):
    P, Y = map(int, input().split())
    dd[P].append([Y, i])

debug_(dd)


ans = [""] * M
for k, vals in dd.items():
    vals.sort()
    for idx, v in enumerate(vals):
        year, seq = v
        idx += 1
        ans[seq] = str(k).zfill(6) + str(idx).zfill(6)

for a in ans:
    print(a)
