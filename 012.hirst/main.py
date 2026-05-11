import random
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
color_list = [(222, 232, 225), (208, 161, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (45, 55, 104), (158, 46, 83), (169, 160, 39), (128, 189, 143), (83, 20, 44), (38, 42, 67), (186, 93, 105), (187, 140, 171), (84, 122, 181), (59, 39, 31), (79, 153, 165), (88, 157, 91), (195, 79, 72), (161, 202, 220), (45, 74, 77), (80, 73, 44), (58, 130, 121), (217, 176, 188), (220, 182, 167), (166, 207, 165)]
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(750)
tim.setheading(0)

number_of_dots_per_line = 10

for row in range(number_of_dots_per_line):
    for dot in range(number_of_dots_per_line):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(number_of_dots_per_line*50)
    tim.setheading(90)
    tim.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()