import random
from turtle import Turtle, Screen
import colorgram

colors = colorgram.extract("image.jpg", 20)

list_color = []

for n in range(0, len(colors)):
    every_color = colors[n]
    rgb = every_color.rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    my_tuple = (r, g, b)
    list_color.append(my_tuple)

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.shape("circle")
tim.shapesize(1)

my_list_colors = list_color


def change_color():
    my_color = random.choice(my_list_colors)
    tim.color(my_color)


tim.speed(0)
change_color()
tim.penup()
tim.setx(-250)
tim.sety(-200)

plus = 0
for number in range(0, 10):
    for n in range(0, 9):
        tim.showturtle()
        tim.speed(1)
        tim.pendown()
        tim.stamp()
        tim.penup()
        tim.forward(50)
        change_color()
        tim.hideturtle()

    tim.speed(0)
    tim.penup()
    tim.setx(-250)
    tim.sety(-150 + plus)
    plus += 50

screen.exitonclick()
