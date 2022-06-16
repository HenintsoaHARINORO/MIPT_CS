import turtle

colors = [
    'violet',  # colors[0]
    'blue',  # colors[1]
    'green',  # colors[2]
    'yellow',  # colors[3]
    'gold',  # colors[4]
    'orange',  # colors[5]
    'red'  # colors[6]
]
wn = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('red')


def sq(size,color):
    for i in range(4):
        t.color(color)
        t.forward(size)
        t.left(90)


def sqn(size, d, n,i):
    if n==0:
        return
    if size <= 0:
        return
    sq(size,colors[i])
    t.penup()
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.pendown()

    sqn(size-(d*2), d , n-1,i+1)


sqn(200, 20, 7,0)

wn.exitonclick()