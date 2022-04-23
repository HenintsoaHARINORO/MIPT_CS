res = 0
n = int(input('n = '))
while n >= 0:
    S = (2 * n + 1) ** 3
    res = S + res
    n += 1
    if n == n:
        break
print(res)