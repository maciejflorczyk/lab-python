import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('hirst.jpg', 30)

rgb_colors = []


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

color_list = [(222, 232, 225), (208, 161, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (45, 55, 104), (158, 46, 83), (169, 160, 39), (128, 189, 143), (83, 20, 44), (38, 42, 67), (186, 93, 105), (187, 140, 171), (84, 122, 181), (59, 39, 31), (79, 153, 165), (88, 157, 91), (195, 79, 72), (161, 202, 220), (45, 74, 77), (80, 73, 44), (58, 130, 121), (217, 176, 188), (220, 182, 167), (166, 207, 165)]
