from turtle import Screen
from playground import Playground
from paddle import Paddle
from ball import Ball
import time


###
# Create screen
# Create paddles
## width = 20
## height = 100
## x_pos =350
## y_pos = 0
# Create ball
# Detect collisions
# Detect collision with paddle
# Keep score
#
# Classes:
# ball
# scoreboard
# paddle
###

from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.title("Pong Game")

playground = Playground()
scoreboard = Scoreboard()
paddle_right = Paddle((350,0))
paddle_left = Paddle((-350,0))

ball = Ball()

screen.listen() #listen for keystrokes
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    #detet collision with right paddle

    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect when right paddle misses
    if ball.xcor() > 380:
        print("Pong")
        scoreboard.increase_score_left()
        ball.reset_position()

    if ball.xcor() < -380:
        print("Pong")
        scoreboard.increase_score_right()
        ball.reset_position()


screen.exitonclick()


