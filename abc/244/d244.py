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


s1, s2, s3 = input().split()
t1, t2, t3 = input().split()

if s1 == t1 and s2 == t2 and s3 == t3:
    print("Yes")
elif s1 == t1 and s2 != t2 and s3 != t3:
    print("No")
elif s1 != t1 and s2 == t2 and s3 != t3:
    print("No")
elif s1 != t1 and s2 != t2 and s3 == t3:
    print("No")
else:
    print("Yes")
