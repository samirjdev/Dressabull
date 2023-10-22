
import colorsys
import matplotlib.pyplot as plt
import numpy as np



#Working on it. #
def generate_three_split_complementary_colors(rgb_color):
    r, g, b = rgb_color
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)

    # Calculate the complementary color
    complementary_hue = (h + 0.5) % 1.0
    complementary_rgb = colorsys.hsv_to_rgb(complementary_hue, s, v)

    # Calculate the two split complementary colors with slight hue shifts
    split_complementary_hue1 = (complementary_hue + 1/6) % 1.0
    split_complementary_hue2 = (complementary_hue - 1/6) % 1.0
    #my WOrking on it.
    split_complementary_hue3 = (complementary_hue + 1/6) % 1.0
    split_rgb1 = colorsys.hsv_to_rgb(split_complementary_hue1, s, v)
    split_rgb2 = colorsys.hsv_to_rgb(split_complementary_hue2, s, v)
    split_rgb3 = colorsys.hsv_to_rgb(split_complementary_hue3, s, v)
    # Scale the RGB values to the range [0, 255]
    complementary_rgb = tuple(int(x * 255) for x in complementary_rgb)
    split_rgb1 = tuple(int(x * 255) for x in split_rgb1)
    split_rgb2 = tuple(int(x * 255) for x in split_rgb2)
    split_rgb3 = tuple(int(x * 255) for x in split_rgb2)

    return [complementary_rgb, split_rgb1, split_rgb2]


#Testing
# # Input RGB color (e.g., human color)
# input_color = (255,219,172)# Blue color

# # Generate three split complementary colors
# three_split_complementary_colors_list = generate_three_split_complementary_colors(input_color)

# # Create a bar chart to visualize the colors
# fig, ax = plt.subplots(figsize=(10, 4))
# for i, color in enumerate(three_split_complementary_colors_list):
#     ax.bar(i, 1, color=[c / 255.0 for c in color])

# # Customize the plot
# ax.set_xlim(-0.5, len(three_split_complementary_colors_list) - 0.5)
# ax.set_xticks(range(len(three_split_complementary_colors_list)))
# ax.set_xticklabels(['Color {}'.format(i) for i in range(1, len(three_split_complementary_colors_list) + 1)])
# ax.set_yticks([])
# ax.set_title("Three Split Complementary Colors")

# # Display the plot
# plt.show()





##Working code

def triadic_colors(rgb_color):
    r, g, b = rgb_color
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)

    # Calculate the two additional colors with 120-degree hue separation
    color1_hue = (h + 1/4) % 1.0
    color2_hue = (h + 2/4) % 1.0
    color3_hue = (h + 3/4) % 1.0

    # Convert back to RGB
    color1 = colorsys.hsv_to_rgb(color1_hue, s, v)
    color2 = colorsys.hsv_to_rgb(color2_hue, s, v)
    color3 = colorsys.hsv_to_rgb(color3_hue, s, v)
    # Scale the RGB values to the range [0, 255]
    color1 = tuple(int(x * 255) for x in color1)
    color2 = tuple(int(x * 255) for x in color2)
    color3 = tuple(int(x * 255) for x in color3)

    return [color1, color2, color3]


#Testing

# # Input RGB color (e.g., human color)
# input_color = (255,219,172)

# # Generate triadic colors
# triadic_colors_list = triadic_colors(input_color)

# # Create a bar chart to visualize the colors
# fig, ax = plt.subplots(figsize=(10, 4))
# for i, color in enumerate(triadic_colors_list):
#     ax.bar(i, 1, color=[c / 255.0 for c in color])

# # Customize the plot
# ax.set_xlim(-0.5, len(triadic_colors_list) - 0.5)
# ax.set_xticks(range(len(triadic_colors_list)))
# ax.set_xticklabels(['Color {}'.format(i) for i in range(1, len(triadic_colors_list) + 1)]
# )
# ax.set_yticks([])
# ax.set_title("Triadic Colors")

# # Display the plot
# plt.show()