import turtle as t
import random
from turtle import Screen

# generate the tuple color list
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
#
# print(rgb_colors)

color_list = [(202, 164, 109), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19),
              (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
              (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
              (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97),
              (176, 192, 209)]

tdot = t.Turtle()
t.colormode(255)
tdot.penup()
tdot.hideturtle()
tdot.speed('fastest')
tdot.setheading(225)
tdot.forward(300)
tdot.setheading(0)


def create_dot():
    tdot.dot(30, random.choice(color_list))
    tdot.penup()
    tdot.forward(50)


def next_line():
    tdot.setheading(90)
    tdot.forward(50)
    tdot.setheading(180)
    tdot.forward(500)
    tdot.setheading(0)


for i in range(10):
    for _ in range(10):
        create_dot()
    next_line()

screen = Screen()
screen.exitonclick()
