number = []
for i in range(10):
    num = int(input())
    number.append(num)
print(number)
max = number[0]
for i in range(len(number)):
   if number[i] >= max:
       max = number[i]
print(max)
