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


K = int(input())

digit = 12

cnt = 0
first = [_ for _ in range(1, 10)]
deq = deque(first)
ans = 0
while deq:
    debug_(deq)
    q = deq.popleft()
    cnt += 1
    if cnt == K:
        ans = q
        break

    if q == 0:
        continue
    else:
        last = q % 10
        if last == 0:
            deq.append(q * 10 + 0)
            deq.append(q * 10 + 1)
        elif last == 9:
            deq.append(q * 10 + 8)
            deq.append(q * 10 + 9)
        else:
            debug_(q * 10 + last - 1)
            debug_(q * 10 + last)
            debug_(q * 10 + last + 1)
            deq.append(q * 10 + last - 1)
            deq.append(q * 10 + last)
            deq.append(q * 10 + last + 1)

print(ans)
