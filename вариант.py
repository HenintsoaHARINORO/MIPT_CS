# Вариант: 3
import turtle        # познакомили программу с библиотекой turtle
wn = turtle.Screen()
t = turtle.Turtle()  # сделали черепаху, назвали черепаху t
#t.shape('turtle')    # как выглядит черепаха
t.color('blue')
t.width(5)
t.forward(100)
t.left(90)
t.color('blue')
t.forward(50)
t.backward(100)
wn.exitonclick()