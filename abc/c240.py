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
dp = [[False for _ in range(X + 1)] for _ in range(N + 1)]

dp[0][0] = True
last_a, last_b = 0, 0
flgs = [True] * 2
last_visit = deque([])
last_visit.append(0)
for i in range(N):
    a, b = map(int, input().split())

    tmp = set()
    while last_visit:
        last_ = last_visit.popleft()

        # if dp[i][last_]:
        if last_ + a <= X:
            debug_(f"i:{i}-1:値を更新します。{last_ + a}")
            dp[i + 1][last_ + a] = True
            tmp.add(last_ + a)

        if last_ + b <= X:
            debug_(f"i:{i}-1:値を更新します。{last_ + b}")
            dp[i + 1][last_ + b] = True
            tmp.add(last_ + b)

    for i in tmp:
        last_visit.append(i)
    debug_("last_visitを更新:\n", last_visit)

    # if flgs[0]:
    #     if dp[i][last_a] and last_a + a <= X:
    #         dp[i + 1][last_a + a] = True

    #     if dp[i][last_a] and last_a + b <= X:
    #         debug_(f"i:{i}-2:値を更新します。")
    #         dp[i + 1][last_a + b] = True

    # if flgs[1]:
    #     if dp[i][last_b] and last_b + a <= X:
    #         debug_(f"i:{i}-3:値を更新します。")
    #         dp[i + 1][last_b + a] = True

    #     if dp[i][last_b] and last_b + b <= X:
    #         debug_(f"i:{i}-4:値を更新します。")
    #         dp[i + 1][last_b + b] = True

    # debug_("", dp)

    # flgs[0], flgs[1] = True, True

    # last_a, last_b = last_a + a, last_b + b
    # if last_a > X:
    #     flgs[0] = False
    # if last_b > X:
    #     flgs[1] = False

if PRINT_DEB:
    for i in dp:
        print(i)

if dp[N][X]:
    print("Yes")
else:
    print("No")
