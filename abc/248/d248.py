import sys
from pprint import pprint
from collections import defaultdict
import bisect

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


N = int(input())
A = list(map(int, input().split()))

x_index = defaultdict(list)
for i, j in enumerate(A):
    x_index[j].append(i)

Q = int(input())
queries = []
for _ in range(Q):
    L, R, X = map(int, input().split())
    L -= 1
    R -= 1
    queries.append([L, R, X])

debug_("", x_index)

for query in queries:
    l, r, x = query

    cnt = 0

    start = bisect.bisect_left(x_index[x], l)
    end = bisect.bisect_right(x_index[x], r)
    # print("start:", start)
    # print("end:", end)
    cnt = end - start
    print(cnt)
