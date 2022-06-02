import turtle        # познакомили программу с библиотекой turtle
wn = turtle.Screen()
t = turtle.Turtle()  # сделали черепаху, назвали черепаху t
t.shape('turtle')    # как выглядит черепаха
t.color('green')
t.width(5)
t.left(60)
t.forward(100)


t.color('red')
t.right(120)
t.forward(100)

t.color('violet')
t.right(120)
t.forward(100)

wn.exitonclick()