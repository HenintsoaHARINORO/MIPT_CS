import turtle

wn = turtle.Screen()
# переменная col запомнит цвет (это текст, нужны ' ')
# переменная size запомнит размер (это число, пишем БЕЗ ' ')
def triangle(col, size):


    t.color(col)   # передаем значение col другой команде
    t.fd(size)     # передаем значение size другой команде
    t.lt(120)
    t.fd(size)     # передаем значение size другой команде
    t.lt(120)
    t.fd(size)     # передаем значение size другой команде
    t.lt(120)


# Здесь закончилась новая команда triangle


# Это место для выполнения команд. Новых и старых.
t = turtle.Turtle()
t.shape('turtle')
t.width(3)

triangle('green', 75)
triangle('red', 100)
triangle('blue', 150)
wn.exitonclick()