number = []
sum = 0
n = int(input('Количество элементов: '))
for i in range(n):
    num = int(input())
    number.append(num)
print(number)
max = number[0]
for i in range(len(number)):
   sum +=number[i]
mean = sum /len(number)
print(mean)
for i in range(len(number)):
   if number[i] >= max:
       max = number[i]
print(max)
