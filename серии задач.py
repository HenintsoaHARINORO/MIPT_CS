n = int(input('n = '))
a = [i **2 for i in range(n)]
for x in a:
    print(x)

n = int(input('n = '))
a = [i **2 for i in range(n)]
print(' '.join(str(x) for x in a))