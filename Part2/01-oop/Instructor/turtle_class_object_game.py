import turtle
import random

turtleObj = turtle.Turtle()

turtleObj.penup()
turtleObj.pencolor('lightblue')
turtleObj. goto(-150,150)

for step in range(15):
  turtleObj.write(step)
  turtleObj.right(90)
  for num in range(8):
    turtleObj.penup()
    turtleObj.forward(10)
    turtleObj.pendown()
    turtleObj.forward(10)
  turtleObj.penup()
  turtleObj.backward(160)
  turtleObj.left(90)
  turtleObj.forward(20)
turtleObj.hideturtle()

#Ist turtle ada

Rahul = turtle.Turtle()
Rahul.color("red")
Rahul.shape("turtle")
Rahul.penup()
Rahul.goto(-165,120)
Rahul.right(360)
Rahul.pendown()
Rahul.write("Rahul   ",align ="right")

# 2nd turtle bob

ajaz = turtle.Turtle()
ajaz.color("turquoise")
ajaz.shape("turtle")
ajaz.penup()
ajaz.goto(-165,90)
ajaz.right(360)
ajaz.pendown()
ajaz.write("ajaz     ",align ="right")

# 3nd turtle bob

apoorv = turtle.Turtle()
apoorv.color("violet")
apoorv.shape("turtle")
apoorv.penup()
apoorv.goto(-165,60)
apoorv.right(360)
apoorv.pendown()
apoorv.write("apoorv  ",align ="right")

# 4th turtle bob

shams = turtle.Turtle()
shams.color("lime")
shams.shape("turtle")
shams.penup()
shams.goto(-165,30)
shams.right(360)
shams.pendown()
shams.write("shams  ",align ="right")

for turn in range(100):
    Rahul.forward(random.randint(1,5))
    ajaz.forward(random.randint(1,5))
    apoorv.forward(random.randint(1,5))
    shams.forward(random.randint(1,5))
