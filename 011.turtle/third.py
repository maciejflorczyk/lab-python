import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

colours = ["red", "blue", "green", "yellow", "black", "orange", "pink", "violet"]

directions = [0,90,180,270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for _ in range(200):

    tim.pensize(15)
    tim.speed(5000)
    tim.forward(25)
    tim.setheading(random.choice(directions))
    tim.pencolor(random_color())



