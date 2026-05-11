#this is a standalone file
from turtle import Screen
import turtle as t
import random

tim = t.Turtle()

colours = ["red", "blue", "green", "yellow", "black", "orange", "pink", "violet"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
        tim.forward(100)


for shape_side_n in range(3,11):
    draw_shape(shape_side_n)
    tim.color(random.choice(colours))



screen = Screen()
screen.exitonclick()
