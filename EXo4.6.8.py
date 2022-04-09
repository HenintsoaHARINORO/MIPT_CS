x = int(input('x= '))
a = int(input('a= '))
k = int(input('k= '))
n = int(input('n= '))
h = int(input('h= '))

xn = x * n
xk = x * k
xh = x * h

an = a * n
ak = a * k
ah = a * h
for x in range(xn, xk + 1, xh):
    for a in range(an, ak + 1, ah):
        y =( x / (((x**2) -49)**0.5) ) + (1/ ((a**2)-100))
        print('a=', a, 'x= ', x, 'y= ', y)