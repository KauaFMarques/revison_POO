'''#Importing turtle
from turtle import *

#Screen size
setup(1.0, 1.0)

bgpic ('2.turn.png')
shape("turtle")
pensize()
color("light green")
penup()
pendown()

#Importing turtle
from turtle import *

#Screen size
setup(1.0, 1.0)
bgpic ('3.plane.png')
shape("turtle")
'''

#Importing turtle
from turtle import *

#Screen size
setup(1.0, 1.0)
bgpic ('4.stars.png')
shape("turtle")

# Print coordinate where clicked:
onscreenclick(lambda x,y: print("x: %d, y: %d" % (x, y)))