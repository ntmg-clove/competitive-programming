import sys
from pprint import pprint
from scipy.special import comb

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


MOD = 10 ** 9 + 7


def gen_comb(n: int, k: int):
    res = 1
    for i in range(k):
        res *= n - i
        # res %= MOD

    for i in range(k):
        res //= i + 1
    res %= MOD
    return res


n, a, b = map(int, input().split())
ans = pow(2, n, MOD) - 1
# ans -= gen_comb(n, a)
ans -= comb(n, a, exact=True) % MOD
# ans -= gen_comb(n, b)
ans -= comb(n, b, exact=True) % MOD
print(ans % MOD) 
# print(gen_comb(n, 100))
# print(gen_comb(n, 5))
# print(gen_comb(n, 10))
