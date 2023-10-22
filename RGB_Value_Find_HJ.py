from PIL import Image

image = Image.open("face_2.jpg")
width, height = image.size
x, y = 100, 100  # Change to the desired coordinates

# Ensure x and y are within the image bounds
x = max(0, min(x, width - 1))
y = max(0, min(y, height - 1))

pixel_color = image.getpixel((x, y))
red, green, blue = pixel_color
print("RGB values at ({}, {}):".format(x, y))
print("Red:", red)
print("Green:", green)
print("Blue:", blue)
