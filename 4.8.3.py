res = 0
n = int(input('n = '))
for n in range(0, n + 1):
    s = (2 * n + 1) ** 3 + (2*n) ** 2
    res = s + res
    print(res)