n = int(input())
s = input()
s1 = s.split(' ')
s2 = list()
s3 = list()
for num in s1:
    s2.append(num)
print(s2)
for num in s2:
    if int(num) % 7 == 0:
        s3.append(int(num))
print(s3)
sum = 0
for num in s3:
    sum += num
print(sum)