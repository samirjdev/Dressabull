
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

# Input RGB color (e.g., human color)
input_color = (255,219,172)

# Generate triadic colors
triadic_colors_list = triadic_colors(input_color)

# Create a bar chart to visualize the colors
fig, ax = plt.subplots(figsize=(10, 4))
for i, color in enumerate(triadic_colors_list):
    ax.bar(i, 1, color=[c / 255.0 for c in color])

# Customize the plot
ax.set_xlim(-0.5, len(triadic_colors_list) - 0.5)
ax.set_xticks(range(len(triadic_colors_list)))
ax.set_xticklabels(['Color {}'.format(i) for i in range(1, len(triadic_colors_list) + 1)]
)
ax.set_yticks([])
ax.set_title("Triadic Colors")

# Display the plot
plt.show()