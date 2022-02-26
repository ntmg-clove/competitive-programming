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


prime_numbers = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281
]

A, B, C, D = map(int, input().split())

tak_win = False
for tak in range(A, B + 1):
    prime_flg = False
    for aok in range(C, D + 1):
        if tak + aok in prime_numbers:
            prime_flg = True
            break
    if not prime_flg:
        tak_win = True
        break

if tak_win:
    print("Takahashi")
else:
    print("Aoki")
