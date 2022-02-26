import sys
from pprint import pprint
import heapq

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

Q = int(input())
queries = []
for _ in range(Q):
    queries.append(list(map(int, input().split())))

A = []
heapq.heapify(A)

for q in queries:
    if q[0] == 1:
        heapq.heappush(A, q[1])
    
    elif q[0] == 2:
        x, k = q[1], q[2]
        pass

    elif q[0] == 3:
        x, k = q[1], q[2]
        pass

