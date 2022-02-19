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

# tree = [[] for _ in range(N)]
tree = {}
for i in X:
    tree[i] = []

for _ in range(N - 1):
    A, B = map(int, input().split())
    tree[A].append(B)
for i in X:
    tree[i].sort(reverse=True)

debug_("", tree)

for _ in range(Q):
    v, k = map(int, input().split())
    