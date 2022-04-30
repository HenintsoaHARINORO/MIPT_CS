number = []
sum = 0
n = int(input('Количество элементов: '))
for i in range(n):
    num = int(input())
    number.append(num)
print(number)
for i in number[-5:10]:
      sum += i
print(sum)
