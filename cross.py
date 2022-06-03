# Вариант: 1
import turtle
wn = turtle.Screen()

t = turtle.Turtle()
t.color('blue')
t.width(8)
def cross():
    t.forward(200)
    t.backward(100)
    t.right(90)
    t.forward(100)
    t.backward(200)

cross()
t.penup()
t.right(45)

t.forward(70)
t.left(45)
t.right(270)
t.pendown()

cross()
t.penup()


t.forward(50)
t.right(90)
t.penup()
t.forward(50)
t.pendown()
t.left(180)

cross()






wn.exitonclick()
