import FD_RGB_V_Combine  as skin_grabber
import GenerateColorPallate as gcp
import ColorConverter as cc
import ImageGenerator as img_gen

skin_color = skin_grabber.grab_skin_color('/home/max/Downloads/PXL_20231022_194530586.MP.jpg')

color_name, color_value = cc.get_clothing_color(skin_color)

print(color_value)  
print(color_name)

gcp.generate_monochromatic_palette(color_value)
gcp.generate_split_complementary_palette(color_value)

colors = gcp.generate_triadic_palette(color_value)

img_gen.main(colors)