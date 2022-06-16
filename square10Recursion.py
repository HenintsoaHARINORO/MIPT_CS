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
    k = len(colors)

    sqn(size-d, d , n-1,i+1)
    sq(size,colors[i])


sqn(200, 20, 7,0)

wn.exitonclick()