#Importing turtle
from turtle import *


#Turtle shape
shape("turtle")

#Screen size
setup(1.0, 1.0)

'''
#challange 1
forward(20)
left(90)
'''

#challange 2
#Background
bgcolor("black")
#House Walls
pensize(15)
pencolor("cyan")
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)

#Roof
pensize(15)
pencolor("magenta")
left(45)
forward(75)
right(90)
forward(75)
hideturtle()
from Quiz import *