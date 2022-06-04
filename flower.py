import turtle
wn = turtle.Screen()

t = turtle.Turtle()
t.shape('turtle')

t.width(3)
def petal():
    t.color('orange')
    t.stamp()
    t.forward(100)
    t.color('red')

def flower():

    t.seth(90)
    petal()
    t.stamp()
    t.penup()
    t.backward(100)
    t.pendown()
    t.seth(60)
    petal()

    t.stamp()
    t.penup()
    t.backward(100)
    t.pendown()
    t.seth(30)
    petal()

    t.stamp()
    t.penup()
    t.backward(100)
    t.pendown()
    t.seth(0)
    petal()

    t.stamp()
    t.penup()
    t.backward(100)
    t.pendown()
    t.seth(-30)
    petal()

    t.stamp()
    t.penup()
    t.backward(100)
    t.pendown()
    t.seth(-60)
    petal()
    t.stamp()
    t.penup()
    t.backward(100)
    t.pendown()
    t.seth(-90)
    petal()



flower()
wn.exitonclick()