x = int(input('x= '))
a = int(input('a= '))
b = int(input('b= '))
k = int(input('k= '))
n = int(input('n= '))
h = int(input('h= '))

xn = x * n
xk = x * k
xh = x * h

an = a * n
ak = a * k
ah = a * h

bn = b * n
bk = b * k
bh = b * h
for x in range(xn, xk + 1, xh):
    for a in range(an, ak + 1, ah):
        for b in range(bn, bk + 1, bh):
            y = 4*(x**2) + 2*a + 5* (b**3)
            print('a=', a, 'x= ', x, 'b= ', b,'y= ', y)