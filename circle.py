import turtle
wn = turtle.Screen()

t = turtle.Turtle()
t.shape('turtle')
t.width(3)


t.color('blue')
t.stamp()           # синий отпечаток


t.fd(50)


t.color('red')
t.dot(10)           # красная точка


t.fd(50)


t.color('green')
t.circle(50)

wn.exitonclick()