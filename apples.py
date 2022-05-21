n = int(input())
s = input()
s2 = s.split()
s3 = list()
s4 = list()
sum = 0
for num in s2:
    s3.append(int(num))
for num in s3:
    sum += num
remain = sum % n
res = sum // n


for k in s3:
    k = res - k
    s4.append(k)
print(' '.join(str(x) for x in s4))
print(remain)

