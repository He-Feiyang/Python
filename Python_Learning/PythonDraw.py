'''
#Draw a python
import turtle
turtle.setup(650, 350, 0, 0)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()
'''

'''
import turtle
turtle.setup(300, 300)
turtle.goto(100, 100)
turtle.goto(100, -100)
turtle.goto(-100, -100)
turtle.goto(-100, 100)
turtle.goto(0, 0)
turtle.done()

import turtle
turtle.circle(100, 180)
turtle.done()
'''


'''
#Draw the letter z
import turtle
turtle.left(45)
turtle.fd(150)
turtle.right(135)
turtle.fd(300)
turtle.left(135)
turtle.fd(150)
turtle.done()
'''


'''
#Draw the number 8
import turtle as t
t.width(15)
t.color("red")
t.circle(100)
t.circle(-100)
t.done()
'''


'''
#Draw a python
import turtle as t
t.setup(800,300,0,0)
t.penup()
t.fd(-250)
t.pendown()
t.seth(-40)
t.pensize(25)
t.pencolor("purple")

for i in range(5):
    t.circle(40, 80)
    t.circle(-40,80)
t.circle(40, 40)
t.fd(40)
t.circle(16,180)
t.fd(40*2/3)
t.done()
'''


'''
#Drwa a square
import turtle as t
t.title("Square")
t.setup(400, 200, 0, 0)
t.penup()
t.fd(-50)
t.right(90)
t.fd(50)
t.left(90)
t.pendown()
t.pensize(10)
t.pencolor('red')
for i in range(4):
    t.fd(100)
    t.left(90)
t.done()
'''
'''
#Draw a colored hexagon
import turtle as t
t.setup(400, 400, 0, 0)
t.title("Draw hexagon")
t.shape("turtle")

t.penup()
t.left(90)
t.fd(100)
t.left(90)
t.fd(50)
t.right(180)
t.pendown()
t.colormode(255) ###set mode 255, default is string
t.pensize(10)

for i in range(6):
    t.pencolor(100 + i * 15, 0 + i * 30, 50 + i * 1)
    t.fd(100)
    t.right(60)
t.done()
'''

'''
#Draw a polygonal
import turtle as t

t.setup(500, 500, 0, 0)
t.title("the one")

t.penup()
t.fd(-50)
t.right(90)
t.fd(50)
t.left(90)
t.pendown()

t.pensize(1)
t.colormode(255)

for i in range(9):
    t.pencolor(255 - i * 5, 0 + i * 5, 255 - i * 4)
    t.fd(100)
    t.left(80)
t.done()
'''

import turtle as t

t.setup(500, 500, 0, 0)
t.title("windmill")

t.pencolor("red")
t.pensize(2)

t.seth(45)
t.fd(150)
t.left(90)
t.circle(150, 45)
t.left(90)
t.fd(300)
t.right(90)
t.circle(-150, 45)
t.right(90)
t.fd(150)

t.right(45)
t.fd(150)
t.right(90)
t.circle(-150, 45)
t.right(90)
t.fd(300)
t.left(90)
t.circle(150, 45)
t.left(90)
t.fd(150)

t.done()