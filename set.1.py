s1 = set()
s2 = set()

v1 = input()
while v1 != '':
    s1.add(v1)
    v1 = input()
s1.add(v1)

v2 = input()
while v2 != '':
    s2.add(v2)
    v2 = input()

result = s1 & s2
if not result:
    print('EMPTY')
else:
    for i in result:
        print(i)
