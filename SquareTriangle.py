import turtle
wn = turtle.Screen()

t = turtle.Turtle()
t.width(5)
def square(col):
    t.color(col)

    t.forward(75)
    t.left(90)

    t.forward(75)
    t.left(90)

    t.forward(75)
    t.left(90)

    t.forward(75)
    t.left(90)
    t.forward(75)

def triangle(col):
    t.color(col)

    t.forward(75)

    t.right(120)
    t.forward(75)

    t.right(120)
    t.forward(75)

square('yellow')
t.backward(75)
t.left(45)
square('green')
t.backward(75)
t.right(165)
triangle('red')
t.right(30)
triangle('blue')



wn.exitonclick()
