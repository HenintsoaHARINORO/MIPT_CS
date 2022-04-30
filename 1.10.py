number = []
sum = 0
flag = 0
n = int(input('Количество элементов: '))
for i in range(n):
    num = int(input())
    number.append(num)
print(number)
for i in number[4:10]:
      sum += number[i]
среднее = sum / len(number[4:10])
print(среднее)
for i in range(len(number)):
    if number[i] == 5:
        flag += 1
print(flag)
