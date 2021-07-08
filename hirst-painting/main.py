import colorgram

# Extract 9 colours from image
extracted_colours = colorgram.extract("image.jpeg", 9)

colours = []
for index, extract in enumerate(extracted_colours):
    colour_extract = extracted_colours[index].rgb
    r, g, b = colour_extract
    colour = (r, g, b)
    colours.append(colour)

print(colours)