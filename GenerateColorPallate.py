import colorsys
import matplotlib.pyplot as plt

def generate_monochromatic_palette(base_color, num_colors=4):
    # Convert the RGB color to HLS color space
    h, l, s = colorsys.rgb_to_hls(base_color[0] / 255.0, base_color[1] / 255.0, base_color[2] / 255.0)

    # Generate a list of harmonious colors with a smaller increment for brightness
    palette = [base_color]
    for i in range(1, num_colors):
        brightness = min(1.0, l + (i * 0.05))  # Adjust the increment for different shades
        r, g, b = colorsys.hls_to_rgb(h, brightness, s)
        palette.append((int(r * 255), int(g * 255), int(b * 255)))

    print(palette)

    draw_palette(palette)


def generate_split_complementary_palette(base_color, num_colors=4):
    # Convert the RGB color to HLS color space
    h, l, s = colorsys.rgb_to_hls(base_color[0] / 255.0, base_color[1] / 255.0, base_color[2] / 255.0)

    # Calculate the two complementary colors by adjusting the hue by 150 and 210 degrees
    complement1_hue = (h + 0.6) % 1.0
    complement2_hue = (h + 0.2) % 1.0

    r1, g1, b1 = colorsys.hls_to_rgb(complement1_hue, l, s)
    r2, g2, b2 = colorsys.hls_to_rgb(complement2_hue, l, s)

    complement1_color = (int(r1 * 255), int(g1 * 255), int(b1 * 255))
    complement2_color = (int(r2 * 255), int(g2 * 255), int(b2 * 255))

    # Generate a list of harmonious colors based on the base color and its complements
    palette = [base_color, complement1_color, complement2_color]

    # Offset for making colors both darker and lighter
    brightness_offset = 0.2  # Adjust as needed

    for i in range(1, num_colors - 2):  # Adjusted the number of colors
        if i % 2 == 0:
            # Make colors darker
            brightness = max(0.0, l - (i // 2 * brightness_offset))
        else:
            # Make colors lighter
            brightness = min(1.0, l + ((i // 2) + 1) * brightness_offset)

        r, g, b = colorsys.hls_to_rgb(h, brightness, s)
        palette.append((int(r * 255), int(g * 255), int(b * 255)))


    print(palette)

    draw_palette(palette)

def generate_triadic_palette(base_color, num_colors=4):
    # Convert the RGB color to HLS color space
    h, l, s = colorsys.rgb_to_hls(base_color[0] / 255.0, base_color[1] / 255.0, base_color[2] / 255.0)

    # Calculate the two triadic colors by adjusting the hue by 120 and 240 degrees
    triad1_hue = (h + 1/3) % 1.0
    triad2_hue = (h + 2/3) % 1.0

    r1, g1, b1 = colorsys.hls_to_rgb(triad1_hue, l, s)
    r2, g2, b2 = colorsys.hls_to_rgb(triad2_hue, l, s)

    triad1_color = (int(r1 * 255), int(g1 * 255), int(b1 * 255))
    triad2_color = (int(r2 * 255), int(g2 * 255), int(b2 * 255))

    # Generate a list of harmonious colors based on the base color and its triadic colors
    palette = [base_color, triad1_color, triad2_color]

    # Offset for making colors both darker and lighter
    brightness_offset = 0.2  # Adjust as needed

    for i in range(1, num_colors - 2):  # Adjusted the number of colors
        if i % 2 == 0:
            # Make colors darker
            brightness = max(0.0, l - (i // 2 * brightness_offset))
        else:
            # Make colors lighter
            brightness = min(1.0, l + ((i // 2) + 1) * brightness_offset)

        r, g, b = colorsys.hls_to_rgb(h, brightness, s)
        palette.append((int(r * 255), int(g * 255), int(b * 255)))

    print(palette)

    draw_palette(palette)

def draw_palette(palette):
    # Example: Generate a monochromatic color palette based on an RGB color

    monochromatic_palette = palette

    # Display the original color and the monochromatic color palette using matplotlib
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.imshow([monochromatic_palette], aspect='auto')
    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()

#draw_palette((76, 175, 80))