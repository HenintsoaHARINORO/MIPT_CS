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
n1 = int(input())
t.color('black')
one_line(n1)
for i in range(n-1):

    size = int(input())

    if n1 < size:
        t.color('red')
    elif n1 > size:
        t.color('blue')
    else:
        t.color('green')

    one_line(size)
wn.exitonclick()
