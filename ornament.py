import turtle
wn = turtle.Screen()

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

def triangle():
    # здесь пишем команды - рисовать треугольник
    # команды надо начать с <TAB> (отступа)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
def ornament():
    # функция рисует 3 треугольника


    t.pencolor('red')
    triangle()          # вызов функции triange
    t.lt(45)


    t.pencolor('green')
    triangle()          # вызов функции triange
    t.lt(45)


    t.pencolor('blue')
    triangle()

ornament()
t.lt(45)
ornament()

wn.exitonclick()