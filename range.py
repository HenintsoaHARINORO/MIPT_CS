import turtle
wn = turtle.Screen()
def write(data):
    t.write(data, font=("Arial", 14, "normal"))

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.color('blue')

for x in range(-30, 200, 40):
    t.goto(x, 0)
    write(x)

wn.exitonclick()