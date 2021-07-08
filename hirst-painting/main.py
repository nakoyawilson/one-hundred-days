# import colorgram
#
# # Extract 10 colours from image
# extracted_colours = colorgram.extract("image.jpeg", 10)
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

colour_list = [(245, 245, 245), (115, 160, 192), (134, 46, 112), (242, 243, 246), (103, 34, 79), (200, 121, 179),
               (163, 62, 43), (18, 25, 48), (122, 121, 127), (244, 238, 242)]

# Create instance of Turtle
paint_brush = turtle.Turtle()
for step in range(10):
    paint_brush.dot(20, random.choice(colour_list))
    paint_brush.penup()
    paint_brush.forward(50)





# Create instance of Screen
screen = turtle.Screen()
screen.exitonclick()