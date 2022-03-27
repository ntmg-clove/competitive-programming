import sys
from pprint import pprint

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


N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

dif_y = 0
dif_x = 0
ans = False
for dif_x in range(N - M + 1):
    for dif_y in range(N - M + 1):

        debug_("----------------------------")
        debug_("A", A)
        debug_("B", B)
        is_break = False
        # 一致判定。1つでも違うものがあれば、ずらす（次のループ）
        for i in range(M):
            for j in range(M):
                if A[i + dif_x][j + dif_y] == B[i][j]:
                    continue
                else:
                    is_break = True
                if is_break:
                    break
            if is_break:
                break
        if not is_break:
            ans = True
            break

if ans:
    print("Yes")
else:
    print("No")
