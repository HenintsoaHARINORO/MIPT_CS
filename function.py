import turtle
wn = turtle.Screen()

# Это новая команда - функция
# Назовем ее triangle()
# def пишем с начала строки без пробелов
def triangle():
    # здесь пишем команды - рисовать треугольник
    # команды надо начать с <TAB> (отступа)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)


# Здесь закончилась новая команда triangle.
# Закончилось определение функции - закончились отступы TAB.


# Это место для выполнения команд. Новых и старых.
t = turtle.Turtle()
t.shape('turtle')
t.pensize(3)
t.color('red')


# выполняется новая команда triangle

t.pencolor('red')
triangle()          # вызов функции triange
t.lt(45)
t.pencolor('green')
triangle()          # вызов функции triange
t.lt(45)
t.pencolor('blue')
triangle()


wn.exitonclick()