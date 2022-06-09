import turtle
wn = turtle.Screen()

# переменная col запомнит цвет
# переменная size запомнит размер отрезка
def dottedLine(col, size):
    t.color(col)   # передаем значение col другой команде


    # рисуем цветную линию
    t.pd()
    t.fd(size)     # передаем значение size другой команде


    # двигаем черепаху на size/2 без рисования
    t.pu()
    t.fd(size/2)   # вычисляем половину size


    # рисуем цветную линию
    t.pd()
    t.fd(size)     # передаем значение size другой команде


    # двигаем черепаху на size/2 без рисования
    t.pu()
    t.fd(size/2)   # вычисляем половину size
# Здесь закончилась новая команда dottedLine


# Это место для выполнения команд. Новых и старых.
t = turtle.Turtle()
t.shape('turtle')
t.width(3)


# вызываем dottedLine для разного цвета и размера
dottedLine('red', 30)
dottedLine('green', 30)
dottedLine('blue', 50)
wn.exitonclick()