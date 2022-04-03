from math import ceil

n = int(input())

end = ceil(n ** (1/3))

ans = end
i = end
x = n
while True:
    j = 0
    while True:
        if x == i ** 3 + i ** 2 + j + i * j ** 2 + j ** 3:
            ans = x
            break
        elif x < i ** 3 + i ** 2 + j + i * j ** 2 + j ** 3:
            break
        j += 1

    x -= 1
