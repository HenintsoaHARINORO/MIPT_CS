import turtle         # познакомили программу с пакетом turtle (черепаха)
wn = turtle.Screen()

t = turtle.Turtle()   # сделали черепаху, назвали черепаху t


t.forward(75)         # вперед 75
t.up()                # поднять карандаш
t.forward(75)         # вперед 75 (линии не видно)
t.down()              # опустить карандаш
t.forward(75)         # вперед 75

wn.exitonclick()