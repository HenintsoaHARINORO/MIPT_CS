if __name__ == '__main__':
    x = 3
    while x <= 9:
        for a in range(-6, 6 +1, 2):
            y = a + (1 / ((x ** 2) - 4))
            print('a=', a, 'x= ',x, 'y= ',y)
            x = x + 1




