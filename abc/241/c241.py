import enum
import sys
from pprint import pprint
from collections import deque

import numpy as np

sys.setrecursionlimit = 10 ** 6

'''MEMO
行列 斜め 判定 
斜め判定は2種類あるので要注意！
'''

PRINT_DEB = True
# PRINT_DEB = False


def debug_(msg: str, ppr: str = None) -> None:
    if not PRINT_DEB:
        return
    print(msg)
    if ppr:
        pprint(ppr)

    return


def is_tateyoko(matrix: list):
    flg = False
    # 横の判定
    for row in matrix:
        cnt = 0
        seq = deque([])
        for i in row:
            # print(row, i, cnt, seq)

            if len(seq) == 6:
                tmp = seq.popleft()
                if tmp == "#":
                    cnt -= 1

            if len(seq) < 6:
                seq.append(i)
                if i == "#":
                    cnt += 1

            if len(seq) == 6:
                if cnt >= 4:
                    flg = True

    return flg


def is_diagonal(matrix: list):
    flg = False
    # 斜めの判定
    n = len(matrix) * 2 - 1

    seq = [_ for _ in range(len(matrix))]
    seq_rev = list(reversed(seq))
    del seq[-1]
    chk_list = seq + seq_rev

    for c in chk_list:
        a, b = 0, c
        cnt = 0
        seq = deque([])
        for _ in range(c + 1):
            # print(a, b)
            i = matrix[a][b]
            # print(i, cnt, seq)

            if len(seq) == 6:
                tmp = seq.popleft()
                if tmp == "#":
                    cnt -= 1

            if len(seq) < 6:
                seq.append(i)
                if i == "#":
                    cnt += 1

            if len(seq) == 6:
                if cnt >= 4:
                    flg = True
            a, b = a + 1, b - 1
    
    rev_seq =  list(reversed([_ for _ in range(len(matrix))]))
    del rev_seq[-1] 
    reveslst = rev_seq + [_ for _ in range(len(matrix))]
    # debug_(reveslst)
    # debug_(chk_list)
    for idx,  c in enumerate(chk_list):
        a, b = 0, reveslst[idx]
        cnt = 0
        seq = deque([])
        for _ in range(c + 1):
            # print(a, b)
            i = matrix[a][b]
            # print(i, cnt, seq)

            if len(seq) == 6:
                tmp = seq.popleft()
                if tmp == "#":
                    cnt -= 1

            if len(seq) < 6:
                seq.append(i)
                if i == "#":
                    cnt += 1

            if len(seq) == 6:
                if cnt >= 4:
                    flg = True

            a, b = a + 1, b + 1
    return flg


N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(input()))

matrix_T = np.array(matrix).T

# 横判定
flg_y = is_tateyoko(matrix)
# print(flg_y)

# 縦判定
flg_t = is_tateyoko(matrix_T)
# print(flg_t)

# 斜め判定
flg_d1 = is_diagonal(matrix)
# 斜め判定

if flg_y or flg_t or flg_d1:
    print("Yes")
else:
    print("No")
