import turtle
colors = [
  'violet',   # colors[0]
  'blue',     # colors[1]
  'green',    # colors[2]
  'yellow',   # colors[3]
  'gold',     # colors[4]
  'orange',   # colors[5]
  'red'       # colors[6]
]
wn = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('red')
def sq(size):
   for i in range(4):
        t.forward(size)
        t.left(90)
def sqn(size,d ,n):
    k = len(colors)
    t1 = t.pos()
    for i in range(n):
        t.color(colors[i % k])
        sq(size- d*i)
        t.forward(size- d*i)
        t.left(90)
        t.goto(t1)
        t.penup()
        t.right(90)
        t.pendown()
sqn(200,20,7)



wn.exitonclick()