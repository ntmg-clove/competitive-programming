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


def knight_forks(x, y):
    lst = []
    lst.append(str([x + 2, y + 1]))
    lst.append(str([x + 1, y + 2]))
    lst.append(str([x + 2, y - 1]))
    lst.append(str([x + 1, y - 2]))
    lst.append(str([x - 2, y + 1]))
    lst.append(str([x - 1, y + 2]))
    lst.append(str([x - 2, y - 1]))
    lst.append(str([x - 1, y - 2]))
    return lst


x1, y1, x2, y2 = map(int, input().split())

k1 = knight_forks(x1, y1)
k2 = knight_forks(x2, y2)

ans = "No"
brk = False
for i in k1:
    for j in k2:
        if i == j:
            ans = "Yes"
            brk = True
        if brk:
            break

    if brk:
        break

print(ans)
