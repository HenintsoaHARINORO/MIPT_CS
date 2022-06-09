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


# в col записываем 'blue', в size записываем 100
triangle('blue', 100)
t.lt(45)


# в col записываем 'red', в size записываем 75
triangle('red', 75)
t.lt(45)


# в col записываем 'green', в size записываем 150
triangle('green', 150)



wn.exitonclick()