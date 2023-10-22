import GenerateColorPallate as gcp
import ColorConverter as cc

skin_color = (255,219,172)

color_name, color_value = cc.get_clothing_color(skin_color)

print(color_value)
print(color_name)

gcp.generate_triadic_palette(color_value)
gcp.generate_split_complementary_palette(color_value)
gcp.generate_monochromatic_palette(color_value)