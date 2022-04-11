import sys
from pprint import pprint
from collections import deque

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


Q = int(input())
queries = []
for _ in range(Q):
    queries.append(list(map(int, input().split())))

deq = deque([])
# deq = []
for q in queries:
    if q[0] == 1:
        x, c = q[1], q[2]
        deq.append([c, x])
    elif q[0] == 2:
        c = q[1]

        pop_cnt = 0
        tmp_sum = 0
        while pop_cnt < c:
            # debug_(f"--------------------")
            # debug_(f"deq:{deq}")
            # debug_(f"c:{c}")
            cnt, x = deq.popleft()
            # debug_(f"cnt, x:{cnt}, {x}")
            if c - pop_cnt < cnt:
                deq.appendleft([cnt - (c - pop_cnt), x])
                tmp_sum += (c - pop_cnt) * x
                pop_cnt += c - pop_cnt
            else:
                tmp_sum += cnt * x
                pop_cnt += cnt

            # debug_(f"pop_cnt:{pop_cnt}")
            # debug_(f"tmp_sum:{tmp_sum}")

        print(tmp_sum)
