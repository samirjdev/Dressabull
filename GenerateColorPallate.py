
import colorsys
import matplotlib.pyplot as plt


def generate_complementary_colors(base_color):
    # Convert the base color to its RGB components
    red, green, blue = base_color
    
    # Calculate the complementary color by inverting each RGB component
    complementary_color = (255 - red, 255 - green, 255 - blue)
    
    #returns the complementary_color
    return complementary_color

# Example usage
#base_color = (255, 0, 0)  # Red
#base_color, complementary_color = generate_complementary_colors(base_color)

#print("Base Color (RGB):", base_color)
#print("Complementary Color (RGB):", complementary_color)



def generate_tetrad_colors(base_color):
    # Convert the base color to its RGB components
    red, green, blue = base_color
    
    # Calculate the other three colors by shifting the hue by 90 degrees
    second_color = ((red + 90) % 256, (green + 90) % 256, (blue + 90) % 256)
    third_color = ((red + 180) % 256, (green + 180) % 256, (blue + 180) % 256)
    fourth_color = ((red + 270) % 256, (green + 270) % 256, (blue + 270) % 256)
    
    #returns the three colors that tetred to the base. 
    return second_color, third_color, fourth_color

# Example usage
#base_color = (255, 0, 0)  # Red
#base_color, second_color, third_color, fourth_color = generate_tetrad_colors(base_color)

#print("Base Color (RGB):", base_color)
#print("Second Color (RGB):", second_color)
#print("Third Color (RGB):", third_color)
#print("Fourth Color (RGB):", fourth_color)





def generate_monochromatic_colors(base_color):
      # Extract the RGB components of the base color
    red, green, blue = base_color

    # Define the factors for adjusting brightness
    factors = [0.6, 0.8, 1.0, 1.2, 1.4]  # You can adjust these factors as needed

    # Create a list to store the generated colors
    colors = []

    for factor in factors:
        new_red = int(min(255, red * factor))
        new_green = int(min(255, green * factor))
        new_blue = int(min(255, blue * factor))
        new_color = (new_red, new_green, new_blue)
        colors.append(new_color)

    #return the color list.
    return colors

# Example usage
#base_color = (255, 0, 0) # Base color (e.g., red)

#generated_colors = generate_monochromatic_colors(base_color)
#print("Generated Colors:")
#for color in generated_colors:
#   print(color)



# def generate_analogous_colors(base_color, num_colors, hue_range=30):
#     # Convert the base RGB color to HSV (Hue, Saturation, Value) format
#     base_hsv = colorsys.rgb_to_hsv(base_color[0] / 255.0, base_color[1] / 255.0, base_color[2] / 255.0)
    
#     # Create a list to store the generated colors
#     analogous_colors = []

#     # Calculate the step size for shifting the hue
#     hue_step = hue_range / (num_colors - 1)
    
#     for i in range(num_colors):
#         # Calculate the new hue
#         new_hue = (base_hsv[0] + (i * hue_step)) % 1.0  # Ensure it wraps around (0-1)
        
#         # Convert the new HSV values back to RGB
#         new_rgb = [int(c * 255) for c in colorsys.hsv_to_rgb(new_hue, base_hsv[1], base_hsv[2])]
        
#         analogous_colors.append(tuple(new_rgb))

#     return analogous_colors

# # Example usage
# base_color = (255, 0, 0)  # Base color (e.g., red)
# num_colors = 5  # Number of analogous colors to generate
# hue_range = 30  # Adjust this to change the degree of similarity between colors

# generated_colors = generate_analogous_colors(base_color, num_colors, hue_range)
# print("Analogous Colors:")
# for color in generated_colors:
#     print(color)


def generate_analogous_colors(base_color, num_colors, hue_range=30):
    # Convert the base RGB color to HSV (Hue, Saturation, Value) format
    base_hsv = colorsys.rgb_to_hsv(base_color[0] / 255.0, base_color[1] / 255.0, base_color[2] / 255.0)
    
    # Create a list to store the generated colors
    analogous_colors = []

    # Calculate the step size for shifting the hue
    hue_step = hue_range / (num_colors - 1)
    
    for i in range(num_colors):
        # Calculate the new hue
        new_hue = (base_hsv[0] + (i * hue_step)) % 1.0  # Ensure it wraps around (0-1)
        
        # Convert the new HSV values back to RGB
        new_rgb = [int(c * 255) for c in colorsys.hsv_to_rgb(new_hue, base_hsv[1], base_hsv[2])]
        
        analogous_colors.append(tuple(new_rgb))

    return analogous_colors

# Example usage
base_color = (255, 0, 0)  # Base color (e.g., red)
num_colors = 5  # Number of analogous colors to generate
hue_range = 30  # Adjust this to change the degree of similarity between colors

generated_colors = generate_analogous_colors(base_color, num_colors, hue_range)

# Create a bar chart to visualize the colors
fig, ax = plt.subplots(figsize=(10, 2))
for i, color in enumerate(generated_colors):
    ax.bar(i, 1, color=[c / 255.0 for c in color])

# Customize the plot
ax.set_xlim(-0.5, len(generated_colors) - 0.5)
ax.set_xticks(range(len(generated_colors)))
ax.set_xticklabels(['Color {}'.format(i) for i in range(1, num_colors + 1)])
ax.set_yticks([])
ax.set_title("Analogous Colors")

# Display the plot
plt.show()