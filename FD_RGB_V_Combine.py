import cv2
import os
from PIL import Image

def grab_skin_color(image):
    # Load the Haar Cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Load an image
    image = cv2.imread(image)

    # Convert the image to grayscale for better detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Create a folder to save the cropped faces (if it doesn't exist)
    if not os.path.exists('cropped_faces'):
        os.mkdir('cropped_faces')

    # Counter for naming the cropped face images
    face_count = 0

    # Initialize variables to keep track of the highest resolution face
    highest_resolution_face = None
    max_width = 0
    max_height = 0

    # Crop and save each detected face as a separate image, and find the highest resolution face
    for (x, y, w, h) in faces:
        face = image[y:y + h, x:x + w]
        cv2.imwrite(f'cropped_faces/face_{face_count}.jpg', face)
        face_count += 1

        # Check if the current face has higher resolution
        if w * h > max_width * max_height:
            max_width, max_height = w, h
            highest_resolution_face = face

    # Save the highest-resolution face as 'highest_resolution_image.jpg'
    if highest_resolution_face is not None:
        cv2.imwrite('cropped_faces/highest_resolution_image.jpg', highest_resolution_face)
        print("Highest resolution face saved as 'highest_resolution_image.jpg'.")

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
    x, y = 500, 900

    # Ensure x and y are within the image bounds
    x = max(0, min(x, highest_resolution_image_pil.width - 1))
    y = max(0, min(y, highest_resolution_image_pil.height - 1))

    # Get the RGB values at the specified coordinates
    pixel_color = highest_resolution_image_pil.getpixel((x, y))
    red, green, blue = pixel_color

    colors = (red, green, blue)

    #Empty the 'cropped_faces' folder after RGB values are printed
    files = os.listdir(cropped_faces_folder)
    for file in files:
        file_path = os.path.join(cropped_faces_folder, file)
        os.remove(file_path)

    return colors

