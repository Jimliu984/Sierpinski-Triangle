import turtle
import time
from turtle import Turtle, color
import random
import numpy as np
### Window Setup ###
window = turtle.Screen()
window.title("Sierpinski Triangle")
turtle.speed(80)
length = 600
### Draw first Triangle ###
turtle.penup()
turtle.goto(0,-250)
turtle.pendown()
turtle.fd(length/2)
turtle.left(120)
turtle.fd(length)
turtle.left(120)
turtle.fd(length)
turtle.left(120)
turtle.fd(length/2)
turtle.right(60)
Points = [turtle.pos()]
length = length/2
### Draw Other Triangles, with 3 around parent triangle ###
def Add_New_Points(Points, length):
    New_Point = [0,0]
    New_Point[0], New_Point[1] = turtle.pos()[0]-(length/2), turtle.pos()[1]
    Points.append(New_Point)
    New_Point = [0, 0]
    New_Point[0], New_Point[1] = turtle.pos()[0]+(length/2), turtle.pos()[1]
    Points.append(New_Point)
    New_Point = [0, 0]
    New_Point[0], New_Point[1] = turtle.pos()[0], turtle.pos()[1]+np.sqrt(length**2-(length/2)**2)
    Points.append(New_Point)
def Draw_Triangle(length):
    for i in range(3):
        turtle.left(120)
        turtle.fd(length)
def Move_To_New_Triangle(Points):
    turtle.penup()
    turtle.goto(Points[0][0],Points[0][1])
    turtle.pendown()
for a in range(5):
    for a in range(np.shape(Points)[0]):
        Move_To_New_Triangle(Points)
        Add_New_Points(Points, length)
        Draw_Triangle(length)
        Points.pop(0)
    length = length/2
turtle.Screen().exitonclick()