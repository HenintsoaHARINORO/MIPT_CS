
import turtle        # познакомили программу с библиотекой turtle

wn = turtle.Screen()
t = turtle.Turtle()  # сделали черепаху, назвали черепаху t
t.shape('turtle')    # как выглядит черепаха
t.color('green')
t.width(5)
t.forward(75)
t.color('red')
t.forward(75)
t.right(45)
t.color('red')
t.forward(75)
wn.exitonclick()