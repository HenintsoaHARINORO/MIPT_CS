if __name__ == '__main__':
    a = -6.0
    n = int(input('n= '))
    k = int(input('k= '))
    x = int(input('x= '))
    while a <= 7:
        for x in range(x* n, (x* k)+1 , 1):
            y = 3 * a + (x*n) ** 0.5
            print('a=', a, 'x= ', x,'xn= ', x * n, 'y= ', y)
            a= a + 0.5