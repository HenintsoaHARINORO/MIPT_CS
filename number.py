number = input()
odd = even = 0
for i in range(0, len(number), 2):
    odd += int(number[i])
print(odd)
for i in range(1, len(number), 2):
    even += int(number[i])
if odd == even:
    print('Счастливый по-питерски!')
else:
    print('Несчастливый по-питерски!')