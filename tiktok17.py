from turtle import *

import turtle

colors=['cyan', 'blue', 'pink', 'yellow','red','green']

tur = turtle.Turtle()
turtle.bgcolor('black')

for i in range(360):
    tur.pencolor(colors[i%6])
    tur.width(i//100 + 1)
    tur.forward(i)
    tur.left(59)