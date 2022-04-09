res = 0
n = int(input("n = "))
for n in range(1, n+1, 1):
    S = ((-1)**n) * 8 * n
    res = S + res
print(res)