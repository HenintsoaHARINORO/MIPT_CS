number = [15,-4,8,4,2,-7,5,9,2,-9]
min = number[0]
for i in range(len(number)):
   if number[i] <= min:
       min = number[i]

print(min)
