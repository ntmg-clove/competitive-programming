import sys
from pprint import pprint

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


N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
X = []

cnt = 0
flg = True
for i, j in zip(A, B):
    if cnt > 0:
        next_ = set()
        for pre in X[-1]:
            flg1 = abs(i - pre) <= K
            flg2 = abs(j - pre) <= K
            if flg1:
                next_.add(i)
            if flg2:
                next_.add(j)
        if next_:
            X.append(list(next_))
        else:
            flg = False
            break
    else:
        X.append([i, j])
    cnt += 1

debug_("", X)
if flg:
    print("Yes")
else:
    print("No")
