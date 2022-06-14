import turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.width(3)

def sq(size,d,col):
    t.begin_fill()
    t.color('gold', col)
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.penup()
    t.left(90)
    t.forward(d)
    t.right(90)
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





wn.exitonclick()