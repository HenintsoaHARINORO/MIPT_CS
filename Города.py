s1 = set()
n = int(input('n = '))
for i in range(n):
    s1.add(input())
print(s1)
n = int(input('n = '))
s2 = set()
for i in range(n):
    s2.add(input())
if s1 == s2:
    print('OK')
else:
    print('Try another')
