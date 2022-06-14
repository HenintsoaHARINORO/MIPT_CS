import turtle

wn = turtle.Screen()


def spiral(n, col):
    t.color(col)
    t.right(90)
    t.forward(15)
    for i in range(n):
        t.color(col)
        t.left(90)
        t.forward(20 + 10 * i)


t = turtle.Turtle()
t.shape('turtle')
t.width(3)
spiral(30, 'red')
wn.exitonclick()
