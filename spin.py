import turtle
wn = turtle.Screen()

t = turtle.Turtle()
t.shape('turtle')
t.color('red')
t.width(3)
def spileft():
    t.forward(25)
    t.right(90)
    t.forward(55)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(100)
def spiright():
    t.forward(100)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(55)
    t.right(90)
    t.forward(25)
def uzorup():
    spileft()
    spiright()


def spidownleft():
    t.forward(25)
    t.left(90)
    t.forward(45)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(100)

def spidownright():
    t.forward(100)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(45)
    t.left(90)
    t.forward(25)

def uzordown():
    spidownleft()
    spidownright()

def uzor():
    uzorup()
    t.penup()
    t.forward(100)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.pendown()
    uzordown()
def uzor2():
    uzor()
    t.penup()
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.pendown()
    uzor()

uzor2()


wn.exitonclick()