from turtle import Turtle


STRETCH_WIDTH = 1
STRETCH_HEIGHT = 5
X_POS_RIGHT = 350
Y_POS_RIGHT = 0
X_POS_LEFT = 350
Y_POS_LEFT = 0


class Paddle(Turtle): #inherit

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(STRETCH_HEIGHT,STRETCH_WIDTH)
        self.showturtle()
        self.up()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
