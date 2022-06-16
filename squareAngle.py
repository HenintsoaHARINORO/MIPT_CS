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
def nextColor(col):
    if col == 'red':
        col = 'gold'
    elif col == 'gold':
        col = 'blue'
    else:
        col ='red'
    return col
def sq(size,color):

        t.color(color)
        t.forward(size)
        t.left(90)



def spi(size,d ,n, col):
    t.color('red')
    if n==0:
        return
    if size <= 10:
        return
    sq(size,col)
    spi(size-(d), d , n-1,nextColor(col))


spi(200, 10, 15,'red')

wn.exitonclick()