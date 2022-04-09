if __name__ == '__main__':
    x = -5
    while x <= 5:
        for a in range(-6, 6 +1, 1):
            y = x **3 + a **2
            print('a=', a, 'x= ',x, 'y= ',y)
            x = x + 1

