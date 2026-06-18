from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Playground():

    def __init__(self):
        self.create_playground()

    def create_playground(self):
        divider = Turtle("square")
        divider.showturtle()
        divider.home()
        divider.color("white")
        divider.pensize(3)
        divider.penup()
        divider.goto(0, 260)
        divider.pendown()
        divider.goto(0, -300)
        divider.penup()
        divider.hideturtle()
