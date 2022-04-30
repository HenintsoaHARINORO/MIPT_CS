English = int(input('Number of English = '))
German = int(input('Number of German = '))
eng = set()
ger = set()
for i in range(English):
    eng.add(input())
for i in range(German):
    ger.add(input())
if len(eng) >= len(ger):
    res = eng - ger
    if len(res) != 0:
        print(len(res))
    else:
        print('NO')
else:
    res = ger - eng
    if len(res) != 0:
        print(len(res))
    else:
        print('NO')

