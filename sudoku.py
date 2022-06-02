a = []
col =[]
col1= []
col2= []
for i in range(0,9):
    a.append([int(j) for j in input().split()])

print(a)

num=0
num1=0
num2=0
num3=0
num4=0
num5=0
for i in range(0,9):
   col.append([col[i] for col in a])
print(col)
blocks = []
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        blocks.append(a[i][j:j + 3] + a[i + 1][j:j + 3] + a[i + 2][j:j + 3])

[print(block) for block in blocks]
for i in range(0,9):
    num=len(col[i])
    num1= len(set(col[i]))
    num2=len(a[i])
    num3= len(set(a[i]))
    num4= len(blocks[i])
    num5 = len(set(blocks[i]))

if num != num1 or num2 != num3 or num4 != num5:
        print('YES')
else:
        print('NO')

