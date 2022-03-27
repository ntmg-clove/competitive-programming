from math import sqrt
import sys
from pprint import pprint

sys.setrecursionlimit = 10 ** 6


# PRINT_DEB = True
PRINT_DEB = False


def enum_all_divs(x: int) -> list:
    i = 1
    front, back = [], []
    while i ** 2 <= x:
        if x % i == 0:
            front.append(i)
            if i != x // i:
                back.append(x // i)
        i += 1
    back.reverse()

    return front + back


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
divs = enum_all_divs(N)

length = len(divs)

debug_(divs)
ans_idx = 0
ans = 0
if sqrt(N) ** 2 == N:
    ans_idx = length // 2
    debug_(ans_idx)
    debug_(N // divs[ans_idx])
    ans = len(str(divs[ans_idx]))
else:
    ans_idx = length // 2 - 1
    debug_(ans_idx)
    debug_(N // divs[ans_idx])
    ans = len(str(max(divs[ans_idx], N // divs[ans_idx])))

print(ans)
