import turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.width(3)
col = input()
size = int(input())
def sq(size,col):
   t.color(col)
   for i in range(4):
        t.forward(size)
        t.left(90)
sq(size,col)
wn.exitonclick()