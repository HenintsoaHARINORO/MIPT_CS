number = []
n = int(input('Количество элементов: '))
for i in range(n):
    num = int(input())
    number.append(num)
print(number)
min = number[0]
for i in range(len(number)):
   if number[i] < min:
       min = number[i]

print(min)

