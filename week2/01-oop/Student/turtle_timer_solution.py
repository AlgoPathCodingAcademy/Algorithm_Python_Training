import turtle
import time

turtleTimer = turtle.Turtle()

seconds = 10
while (seconds > 0):
  turtleTimer.clear()
  turtleTimer.write(seconds)
  time.sleep(1)
  seconds = seconds - 1
  
turtleTimer.clear()
turtleTimer.write(seconds)
