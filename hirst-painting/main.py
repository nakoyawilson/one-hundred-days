# import colorgram
#
# # Extract 30 colours from image
# extracted_colours = colorgram.extract("image.jpeg", 30)
#
# colours = []
# for index, extract in enumerate(extracted_colours):
#     colour_extract = extracted_colours[index].rgb
#     r, g, b = colour_extract
#     colour = (r, g, b)
#     colours.append(colour)
# print(colours)

import random
import turtle

# Change colormode so that rgb colours can be used
turtle.colormode(255)

colour_list = [(251, 241, 246), (245, 252, 249), (243, 235, 74), (211, 158, 93),
               (186, 12, 69), (112, 179, 208), (25, 116, 168), (173, 171, 31), (219, 129, 166), (161, 79, 35),
               (129, 185, 146), (9, 32, 76), (222, 62, 105), (235, 73, 42), (180, 45, 94), (30, 136, 81),
               (236, 164, 193), (78, 12, 63), (12, 54, 33), (234, 227, 7), (26, 165, 209), (16, 43, 132), (58, 166, 96),
               (134, 214, 229), (10, 101, 63), (133, 34, 20), (91, 27, 11), (159, 211, 188)]

# Create instance of Turtle
paint_brush = turtle.Turtle()

# Change paint_brush speed
paint_brush.speed("fastest")

# Hide turtle
paint_brush.hideturtle()

def create_row():
    for step in range(10):
        paint_brush.dot(20, random.choice(colour_list))
        paint_brush.penup()
        paint_brush.forward(50)

paint_brush.penup()
y_coordinate = -250
while y_coordinate < 250:
    paint_brush.setposition(-250, y_coordinate)
    create_row()
    y_coordinate += 50

# Create instance of Screen
screen = turtle.Screen()
screen.exitonclick()