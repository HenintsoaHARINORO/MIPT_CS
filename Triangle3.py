import turtle

wn = turtle.Screen()
size= int(input())
col1 = input()
col2 = input()
def triangle( size,col1,col2):
    t.begin_fill()
    t.color(col1,col2)
    t.fd(size)     # передаем значение size другой команде
    t.lt(120)
    t.fd(size)     # передаем значение size другой команде
    t.lt(120)
    t.fd(size)     # передаем значение size другой команде
    t.lt(120)
    t.end_fill()


t = turtle.Turtle()
t.shape('turtle')
t.width(3)


triangle(size,col1,col2)





wn.exitonclick()