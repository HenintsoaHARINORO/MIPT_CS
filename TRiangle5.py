import turtle
import math
wn = turtle.Screen()
size1 = int(input())
size2 = int(input())
def hyp(size1,size2):
   res = size1*size1 +size2*size2
   return math.sqrt(res)
a = hyp(size1,size2)
def triangle(col, size1,size2):

    t.color(col)   # передаем значение col другой команде
    t.fd(size1)     # передаем значение size другой команде
    t.lt(90)
    t.fd(size2)     # передаем значение size другой команде
    t.left(135)
    t.fd(a)

def write(text):
    t.write(text, font=('Arial', 18, 'normal'))
t = turtle.Turtle()
t.shape('turtle')
t.width(3)

triangle('red', size1,size2)

write(a)
print(a)
wn.exitonclick()