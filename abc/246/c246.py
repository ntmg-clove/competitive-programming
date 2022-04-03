n, k, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

ans = 0
limit = k
fin = False
rest = []
for i in a:
    tmp = i // x
    # print('-------------------------') # MARK
    # print("tmp", tmp) # MARK
    # print(tmp * x) # MARK
    if tmp > 0 and tmp <= limit:
        # print('tmp a', tmp) # MARK
        limit -= tmp
        if i - tmp * x > 0:
            rest.append(i - tmp * x)
    elif limit > 0 and tmp > limit:
        # print('limit', limit) # MARK
        rest.append(i - limit * x)
        # print('rest', rest) # MARK
        limit = 0
    else:
        rest.append(i)
        # print(rest) # MARK

    # print('rest', rest) # MARK
    # print('tmp', tmp) # MARK
    # print('limit', limit) # MARK
    # print('ans', ans) # MARK

rest.sort(reverse=True)

for i in rest:
    if limit > 0:
        limit -= 1
    else:
        ans += i

print(ans)
