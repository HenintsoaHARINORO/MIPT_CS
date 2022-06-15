import turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.width(3)
def changeColor(col):
    if col =='red':
        col = 'yellow'
    else:
        col = 'red'
    return col
def sq(size,col):
    t.begin_fill()
    t.color('gold', col)
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.penup()
    t.forward(size)
    t.pendown()

    t.end_fill()
def sq2(size,n):
    i= 0
    col ='red'
    while i < n:
        sq(size,col)
        col = changeColor(col)
        i += 1
    t.left(90)
    t.forward(size)
    i =0
    while i < (n-1):
        sq(size,col)
        col = changeColor(col)
        i +=1
    t.left(90)
    t.forward(size)
    i = 0
    while i < (n - 2):
        sq(size, col)
        col = changeColor(col)
        i += 1
    t.left(90)
    t.forward(size)
    i = 0
    while i < (n - 3):
        sq(size, col)
        col = changeColor(col)
        i += 1
    t.left(90)
    t.forward(size)
    i = 0
    while i < (n - 4):
        sq(size, col)
        col = changeColor(col)
        i += 1
    t.left(90)
    t.forward(size)
    i = 0
    while i < (n - 5):
        sq(size, col)
        col = changeColor(col)
        i += 1
    t.left(90)
    t.forward(size)
    i = 0
    while i < (n - 6):
        sq(size, col)
        col = changeColor(col)
        i += 1
    t.left(90)
    t.forward(size)
    i = 0
    while i < (n - 7):
        sq(size, col)
        col = changeColor(col)
        i += 1
sq2(25,8)
wn.exitonclick()
