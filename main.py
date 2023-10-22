import FD_RGB_V_Combine  as skin_grabber
import GenerateColorPallate as gcp
import ColorConverter as cc

skin_color = skin_grabber.grab_skin_color()

color_name, color_value = cc.get_clothing_color(skin_color)

print(color_value)  
print(color_name)

gcp.generate_triadic_palette(color_value)
gcp.generate_split_complementary_palette(color_value)
gcp.generate_monochromatic_palette(color_value)