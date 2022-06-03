import turtle
wn = turtle.Screen()

t = turtle.Turtle()
t.shape('turtle')
t.color('blue')
t.width(3)

def pik():
    t.left(60)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.left(60)
def gory():
    pik()
    pik()
    pik()
gory()
wn.exitonclick()