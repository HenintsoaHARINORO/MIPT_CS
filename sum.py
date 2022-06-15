import turtle
wn = turtle.Screen()


d = 30


def write(text):
    t.write(text, font=('Arial', 18, 'normal'))



def one_line(size):
    x = t.xcor()
    y = t.ycor()

    write(size)
    print(f'draw line size={size} from {x},{y}')  # не работает в repl.it
    # print(size, x, y)                           # для repl.it

    t.fd(size)
    t.pu()
    t.goto(x, y - d)
    t.pd()


t = turtle.Turtle()
t.shape('turtle')
t.width(5)
t.color('blue')


# читаем 1 число n
n = int(input())
# в цикле n раз читаем число и рисуем отрезок
for i in range(n):
    size = int(input())
    if size <0 :
        t.color('blue')

    else:
        t.color('red')
    one_line(size)
wn.exitonclick()

