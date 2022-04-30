number = []
number2= []
sum = 0
res = 1
n = int(input('Количество элементов: '))
for i in range(n):
    num = int(input())
    number.append(num)
print(number)
for i in range(len(number)):
    if number[i] < 0:
        number2.append(number[i])
for i in range(len(number2)):
      sum += number2[i]
среднее = sum / len(number2)
print(number2)
print(sum)
print(среднее)