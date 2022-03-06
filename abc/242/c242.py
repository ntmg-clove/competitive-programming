import sys
from pprint import pprint

sys.setrecursionlimit = 10 ** 6

MOD = 998244353
# PRINT_DEB = True
PRINT_DEB = False


def debug_(msg: str, ppr: str = None) -> None:
    if not PRINT_DEB:
        return
    print(msg)
    if ppr:
        pprint(ppr)

    return


N = int(input())

counts = [1] * 9
for _ in range(N - 1):
    debug_(sum(counts), counts)
    next_ = [0] * 9
    next_[0] += counts[0] + counts[1]
    next_[0] %= MOD

    for i in range(2, 9):
        next_[i - 1] += counts[i - 2] + counts[i - 1] + counts[i]
        next_[i - 1] %= MOD

    next_[8] += counts[7] + counts[8]
    next_[8] %= MOD

    counts = next_

print(sum(counts) % MOD)
