import turtle
wn = turtle.Screen()

def stamped():
    t.color('red')
    t.stamp()           # отпечаток
    t.fd(100)           # линия


    t.color('green')
    t.stamp()           # отпечаток
    t.fd(100)           # линия


    t.color('gold')
    t.stamp()           # отпечаток
    t.fd(100)           # линия


    t.color('blue')
    t.stamp()           # отпечаток
    t.fd(100)           # линия


t = turtle.Turtle()
t.shape('turtle')
t.width(3)


stamped()
wn.exitonclick()