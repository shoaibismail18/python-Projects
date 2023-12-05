import turtle as t
import random
tim=t.Turtle()
t.colormode(255)
def random_colour():
     r=random.randint(0,255)
     g = random.randint(0, 255)
     b = random.randint(0, 255)
     colour=(r,g,b)
     return colour

directions=[0,90,180,270,]
tim.speed("fastest")

for i in range(100):
    tim.color(random_colour())
    tim.circle(100)
    current_heading=tim.heading()
    tim.setheading(current_heading+10)

screen=t.Screen()
screen.exitonclick()