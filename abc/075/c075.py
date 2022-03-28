import sys
from pprint import pprint
from collections import deque

sys.setrecursionlimit = 10 ** 6

# unionfind
# 橋検出

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


N, M = map(int, input().split())

paths = [[] for _ in range(N)]

ans = 0
links = []
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    links.append([a, b])
    paths[a].append(b)
    paths[b].append(a)

for l in links:
    a, b = l

    deq = deque([])
    deq.append(0)
    visits = [False] * N
    # visits[0] = True
    while deq:
        q = deq.popleft()
        if not visits[q]:
            for i in paths[q]:
                if q == a and i == b or q == b and i == a:
                    pass
                    # print("取り除かれています")
                else:
                    deq.append(i)
        visits[q] = True

    if sum(visits) != N:
        ans += 1


print(ans)
