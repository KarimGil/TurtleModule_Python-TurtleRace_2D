import turtle
import time
from random import randint


#Setting Up Display
window = turtle.Screen() #creates graphic screen
window.title("TURTLE RACE") #this is for window title
window.bgcolor("forestgreen") #adds background color to window
turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140,200) #set position for turtle
turtle.write("TURTLE RACE", font=("Arial",30, "bold")) #Game title in screen


#DIRT #Creating dirt in background
turtle.penup()
turtle.setpos(-400,-180)
turtle.color("chocolate")
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(3000)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(3000)
turtle.right(90)
turtle.end_fill()

#Finish Line
stamp_size = 20
square_size = 15
finish_line = 200

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size/stamp_size)
turtle.penup()

for i in range(10):
    turtle.setpos(finish_line,(150-(i*square_size*2)))
    turtle.stamp()

for j in range(10):
    turtle.setpos(finish_line + square_size, ((150-square_size)-(j * square_size *2)))
    turtle.stamp()

turtle.hideturtle()

#Turtle 1

turtle1 = turtle.Turtle()
turtle1.speed(0)
turtle1.color("black")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250,100)
turtle1.pendown()

#Turtle 2

turtle2 = turtle.Turtle()
turtle2.speed(0)
turtle2.color("cyan")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250,50)
turtle2.pendown()

#Turtle 3

turtle3 = turtle.Turtle()
turtle3.speed(0)
turtle3.color("magenta")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250,0)
turtle3.pendown()

#Turtle 4

turtle4 = turtle.Turtle()
turtle4.speed(0)
turtle4.color("yellow")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250,-50)
turtle4.pendown()

time.sleep(1)

#Move the turtle

for i in range(145):
    turtle1.forward(randint(1,5))
    turtle2.forward(randint(1,5))
    turtle3.forward(randint(1,5))
    turtle4.forward(randint(1,5))

turtle.exitonclick()
