n = int(input())
s = input().split(' ')
s2 = []
for num in s:
    s2.append(int(num))
print(s2)

s4 = []
s5 = []
for j in range(n-3+1):
        sum = 0
        s4 = s2[j:j + 3]
        print(s4)

        for k in s4:

            sum += int(k)

        s5.append(sum)
print(s5)
s9 = []
pivot = 0
num= 0
flag = 0
for i in range(len(s5)-1):
    if s5[i] <= s5[i+1]:
        pivot = s5[i+1]

for i in range(len(s5)):
    if s5[i] == pivot:
        flag +=1
        s9.append(i)
        print('i',i)
print(pivot)
print(s9)

print('flag',flag)
if len(s9) == 0:
    print(s)
else:
    for i in range(len(s9)):
        s= s2[s9[i]:s9[i] +3]
        s1 = ' '.join(str(x) for x in s)
        print(s1)




