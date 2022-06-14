import turtle
wn = turtle.Screen()

def write(data):
    t.write(data, font=("Arial", 14, "normal"))


def nextColor(col):
    if col == 'red':  # после красного
        col = 'gold'  # цвет желтый
    else :            # иначе (не красный)
        col = 'red'   # цвет красный
    return col

def dashes(n,col):
    for i in range(n):

        t.color(col)
        write(i)
        t.fd(50)
        col = nextColor(col)


t = turtle.Turtle()
t.shape("turtle")
t.width(3)


dashes(5, 'gold')
wn.exitonclick()