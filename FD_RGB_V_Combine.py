import cv2
import os
from PIL import Image

# Load the Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load an image
image = cv2.imread('Test_Image1.jpeg')

# Convert the image to grayscale for better detection
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Create a folder to save the cropped faces (if it doesn't exist)
if not os.path.exists('cropped_faces'):
    os.mkdir('cropped_faces')

# Counter for naming the cropped face images
face_count = 0

# Crop and save each detected face as a separate image
for (x, y, w, h) in faces:
    face = image[y:y + h, x:x + w]
    cv2.imwrite(f'cropped_faces/face_{face_count}.jpg', face)
    face_count += 1

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with detected faces
# cv2.imshow('Face Detection', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Path to the folder containing cropped face images
cropped_faces_folder = 'cropped_faces'

# Ensure the folder exists
if not os.path.exists(cropped_faces_folder):
    print(f"'{cropped_faces_folder}' folder not found.")
else:
    # Get a list of files in the folder
    files = os.listdir(cropped_faces_folder)

    # Initialize variables to keep track of the highest resolution image
    highest_resolution_image = None
    max_width = 0
    max_height = 0

    # Iterate through the images to find the one with the highest resolution
    for filename in files:
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
            filepath = os.path.join(cropped_faces_folder, filename)
            image = cv2.imread(filepath)

            # Get the dimensions of the image
            height, width, _ = image.shape

            # Check if the current image has higher resolution
            if width * height > max_width * max_height:
                max_width, max_height = width, height
                highest_resolution_image = image

    # Check if a high-resolution image was found
    if highest_resolution_image is not None:
        # Save the highest-resolution image as a separate image
        save_path = os.path.join(cropped_faces_folder, 'highest_resolution_image.jpg')
        cv2.imwrite(save_path, highest_resolution_image)
        print(f"Highest resolution image saved as 'highest_resolution_image.jpg' in '{cropped_faces_folder}'.")
    else:
        print("No valid images found in the folder or no higher resolution image detected.")

# Open the highest-resolution image using PIL
highest_resolution_image_pil = Image.open(os.path.join(cropped_faces_folder, 'highest_resolution_image.jpg'))

# Desired coordinates for pixel inspection
x, y = 100, 100

# Ensure x and y are within the image bounds
x = max(0, min(x, highest_resolution_image_pil.width - 1))
y = max(0, min(y, highest_resolution_image_pil.height - 1))

# Get the RGB values at the specified coordinates
pixel_color = highest_resolution_image_pil.getpixel((x, y))
red, green, blue = pixel_color

# Print the RGB values
print("RGB values at ({}, {}):".format(x, y))
print("Red:", red)
print("Green:", green)
print("Blue:", blue)
print("--------")
colors = (red, green, blue)
print(colors)

# Empty the 'cropped_faces' folder after RGB values are printed
files = os.listdir(cropped_faces_folder)
for file in files:
    file_path = os.path.join(cropped_faces_folder, file)
    os.remove(file_path)
