import sys
from pprint import pprint
from collections import deque

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


N, X = map(int, input().split())
# S = input()

buff = list(bin(X)[2:])
for s in input():
    if s == "U":
        buff.pop()
    elif s == "L":
        buff.append("0")
    elif s == "R":
        buff.append("1")

ans = "".join(buff)
# digit = 0
# while buff:
#     i = buff.pop()
#     if i == "1":
#         ans += 2 ** digit
#     digit += 1

print(int(ans, 2))
