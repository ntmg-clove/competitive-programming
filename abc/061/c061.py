import sys
from pprint import pprint
from collections import Counter

sys.setrecursionlimit = 10 ** 6


PRINT_DEB = True
# PRINT_DEB = False


def debug_(msg: str, ppr: str = None) -> None:
    if not PRINT_DEB:
        return
    print(msg, end="")
    if ppr:
        pprint(ppr)
    else:
        print()

    return


N, K = map(int, input().split())
nums = set()
counter = Counter()

for _ in range(N):
    a, b = map(int, input().split())
    nums.add(a)
    counter[a] += b

nums = list(nums)
nums.sort()

now = K
ans = 0
for n in nums:
    if counter[n] >= now:
        ans = n
        break
    else:
        now -= counter[n]

print(ans)
