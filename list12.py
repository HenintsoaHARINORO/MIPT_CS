squares = []
for i in range(8):
    print(i)
    squares.append(i**2)
print(squares)


cubic = [i**3 for i in range(8)]
print(cubic)

even = [i for i in range(10) if i % 2 ==0]
print(even)

a= [int(x) for x in '764 90 23 4'.split()]
print(a[2])

a1,a2,a3,a4= [int(x) for x in '764 90 23 4'.split()]
print(a1,a2,a3,a4,sep='\n')

print(','.join(str(i) + '^2= '+ str(i**2) for i in range(1,10)))

message = input()
words = message.split()
secret_words = words[2::3]
secret_message = ' '.join(secret_words)
print(secret_message)

print(' '.join(input().split()[2::3]))