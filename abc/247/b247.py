import sys
from pprint import pprint

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


N = int(input())
s_lst = []
t_lst = []
for _ in range(N):
    s, t = input().split()
    s_lst.append(s)
    t_lst.append(t)

ans = True
a = []
for i in range(N):
    tmp_s_lst = s_lst[:]
    del tmp_s_lst[i]
    tmp_t_lst = t_lst[:]
    del tmp_t_lst[i]

    tmp_a_lst = ["", ""]

    if s_lst[i] not in tmp_s_lst and s_lst[i] not in tmp_t_lst:
        tmp_a_lst[0] = s_lst[i]
    if t_lst[i] not in tmp_s_lst and t_lst[i] not in tmp_t_lst:
        tmp_a_lst[1] = t_lst[i]

    if tmp_a_lst[0] or tmp_a_lst[1]:
        a.append(tmp_a_lst)
    else:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")
