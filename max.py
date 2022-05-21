s5= [6,8 ,8,6]
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
        print(i)
print(pivot)
print(s9)
print(flag)
