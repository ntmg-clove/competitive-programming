from collections import deque
from http.client import PROCESSING
import sys
from pprint import pprint

from numpy import delete

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


N = int(input())
a = list(map(int, input().split()))

cylinder = deque([])

reach = 0
seq = 0
last = None
delete_num = 0
cnt = 0
history = deque([])
for idx, ball in enumerate(a):
    if PRINT_DEB:
        print("ball", "last", "reach", "cylinder")
        print(ball, last, reach, history)
    if len(history) >= 1:
        if history[-1][0] == ball:
            history[-1][1] += 1
            cnt += 1

            if history[-1][0] == history[-1][1]:    
                cnt -= ball
                history.pop()
        
        else:
            history.append([ball, 1])
            cnt += 1

    else:
        history.append([ball, 1])
        cnt += 1
    
    print(cnt)
