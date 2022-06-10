import turtle
wn = turtle.Screen()
def cross(size):
        t.fd(size)
        t.bk(size)
        t.lt(90)


        t.fd(size)
        t.bk(size)
        t.lt(90)


        t.fd(size)
        t.bk(size)
        t.lt(90)


        t.fd(size)
        t.bk(size)
        t.lt(90)

def uzor_draft():
        t.color('blue')
        cross(150)


        t.color('red')
        t.rt(150)
        t.fd(150+75)
        t.seth(0)


        t.color('blue')
        cross(75)


        t.color('red')
        t.lt(90)
        t.fd(150+75)
        t.seth(0)


        t.color('blue')
        cross(40)

def snowline(x):
        t.fd(2*x)       # --


        t.lt(45)        #   /
        t.fd(x)
        t.bk(x)


        t.rt(45)        #   -
        t.fd(x)
        t.bk(x)


        t.rt(45)        #   \
        t.fd(x)
        t.bk(x)


        t.lt(45)        # --
        t.bk(2*x)

def snowflake(size):
        snowline(size/3)
        t.lt(60)
        snowline(size/3)
        t.lt(60)
        snowline(size/3)
        t.lt(60)
        snowline(size/3)
        t.lt(60)
        snowline(size/3)
        t.lt(60)
        snowline(size/3)
        t.lt(60)
def uzor():
        snowflake(150)


        t.pu()
        t.rt(150)
        t.fd(150+75)
        t.seth(0)
        t.pd()


        snowflake(75)


        t.pu()
        t.lt(90)
        t.fd(150+75)
        t.seth(0)
        t.pd()


        snowflake(40)



t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')
t.speed(0)

uzor()


wn.exitonclick()
