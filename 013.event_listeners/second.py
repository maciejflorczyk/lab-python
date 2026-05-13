from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = {}

is_race_on = False

for index, color in enumerate(colors):
    turtles[color] = Turtle(shape="turtle")
    turtles[color].color(color)
    turtles[color].penup()
    turtles[color].goto(x=(-230), y=140-index*50)

if user_bet:
    is_race_on = True

while is_race_on:


        for color in colors:
            turtles[color].forward(random.randint(0, 10))
            if turtles[color].xcor() >= 230:
                winner = turtles[color].pencolor()
                if winner == user_bet:
                    print(f"You won! The {winner} is the winner turtle!")
                else:
                    print(f"You lost! The {winner} is the winner turtle!")
                is_race_on = False


screen.exitonclick()
