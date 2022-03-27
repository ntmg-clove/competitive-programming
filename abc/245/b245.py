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


lists = [True for _ in range(2001)]

N = int(input())
A = list(map(int, input().split()))

for a in A:
    lists[a] = False

ans = 0
for i, j in enumerate(lists):
    if j:
        ans = i
        break

print(ans)
