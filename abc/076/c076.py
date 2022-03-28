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


S = input()
T = input()

yn = False
S_rev = S[::-1]
T_rev = T[::-1]

idx = 0
while idx < len(S) - len(T) + 1 and not yn:

    S_rev_tmp = S_rev[idx : idx + len(T)]
    arr_replace = []
    debug_("S_rev_tmp", S_rev_tmp)
    debug_("T_rev", T_rev)
    for s, t in zip(S_rev_tmp, T_rev):
        debug_("s, t", [s, t])
        if s == t or s == "?":
            arr_replace.append(t)
        else:
            break
    else:
        yn = True
    idx += 1

S_rev_arr = list(S_rev)
if yn:
    S_rev_arr[idx - 1 : idx + len(T) - 1] = T_rev

debug_("S_rev_arr", S_rev_arr)
ans = "".join(S_rev_arr[::-1]).replace("?", "a")

if yn:
    print(ans)
else:
    print("UNRESTORABLE")
