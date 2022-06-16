n = int(input())
n1 = int(input())
print(f'{n1} first')

for i in range(n-1):
    num = int(input())
    if num > n1:
        print(f'{num} >')
    elif num < n1:
        print(f'{num} <')
    else:
        print(f'{num} =')