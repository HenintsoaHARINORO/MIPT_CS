number = []
flag = 0
n = int(input('Number of element: '))
for i in range(n):
    num = int(input())
    number.append(num)
print(number)
for i in range(len(number)):
    if number[i] >= 0:
        flag += 1
print(flag)
