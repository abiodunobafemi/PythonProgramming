#Turtle Art - Playing with the Turtle library
from turtle import *
import turtle 

for i in range(4):
   forward(150)
   right(90)
done()


#Star
anms = turtle.Turtle()
anms.speed(10)

for i in range(8):
   anms.forward(200)
   anms.left(135)

turtle.mainloop()
