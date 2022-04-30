number = []
sum = 0
product = 1
n = int(input('Количество элементов: '))
for i in range(n):
    num = int(input())
    number.append(num)
print(number)
for i in number[-2:8]:
      sum += number[i]
      product *= number[i]

среднее = sum / len(number[-2:8])
print(среднее)
print(product)
