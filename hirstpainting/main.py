# import colorgram
import turtle
from turtle import Turtle, Screen
import random
# rgb_colors = []
# colors = colorgram.extract('hirst.png', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)
my_turtle = Turtle()
screen = Screen()
color_list = [(240, 242, 245), (0, 0, 0), (225, 236, 229), (142, 176, 208), (25, 32, 48), (235, 229, 214), (24, 107, 160), (208, 163, 113), (143, 30, 63), (235, 220, 233), (230, 211, 92), (3, 162, 197), (219, 58, 82), (228, 81, 42), (54, 167, 115), (27, 61, 118), (195, 127, 167), (170, 54, 98), (106, 181, 86), (109, 99, 87), (240, 204, 2), (193, 187, 47), (1, 102, 119), (18, 21, 20), (48, 151, 109), (174, 212, 170), (116, 38, 37), (57, 39, 64), (220, 173, 189), (153, 206, 219)]
turtle.colormode(255)
my_turtle.shape('circle')
my_turtle_size = 20
my_turtle.penup()
my_turtle.goto(-250, -250)
my_turtle.speed("fastest")
for x in range(10):
    my_turtle.color(random.choice(color_list))
    my_turtle.stamp()
    for _ in range(9):
        my_turtle.color(random.choice(color_list))
        my_turtle.penup()
        my_turtle.forward(55)
        my_turtle.stamp()
    if x % 2 != 0:
        if x < 9:
            my_turtle.right(90)
            my_turtle.forward(55)
            my_turtle.right(90)
    else:
        my_turtle.left(90)
        my_turtle.forward(55)
        my_turtle.left(90)




screen.exitonclick()