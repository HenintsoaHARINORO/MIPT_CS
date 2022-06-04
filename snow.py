import turtle
wn = turtle.Screen()

t = turtle.Turtle()
t.shape('turtle')
t.color('blue')
t.width(3)

def snowline():
    t.forward(150)
    t.left(180)
    t.forward(45)
    t.right(135)
    t.forward(45)
    t.right(180)
    t.forward(45)
    t.left(135)
    t.right(45)
    t.forward(50)
    t.backward(50)
    t.right(135)

    t.forward(100)
    t.right(180)

def snowflake():
    snowline()
    t.left(58)
    t.backward(3)
    snowline()
    t.left(60)
    t.backward(3)
    snowline()
    t.left(61)
    t.backward(3)
    snowline()
    t.left(61)
    t.backward(3)
    snowline()
    t.left(61)
    t.backward(3)
    snowline()



snowflake()
wn.exitonclick()