from operator import indexOf
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


a = list(map(int, input().split()))

now = a[0]
# print(now)
now = a[now]
# print(now)
now = a[now]
print(now)