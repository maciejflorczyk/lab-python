from turtle import Turtle, Screen


timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")



for i in range(4):
    timmy.pu()
    timmy.forward(10)
    timmy.pd()
    timmy.forward(10)
    timmy.pu()


screen = Screen()
screen.exitonclick()
