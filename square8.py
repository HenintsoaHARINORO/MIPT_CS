import turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.width(3)

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

def NextCol(col):
    if col == 'red':
        col= 'gold'
    elif col == 'gold':
        col = 'green'
    else:
        col = 'red'
    return col
def csq_row(size,n):
    col = 'red'
    for i in range(n):
        sq(size,col)
        col = NextCol(col)
        print(col)
csq_row(50,7)





wn.exitonclick()