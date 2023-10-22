import cv2
import numpy as np

# Load the image
image = cv2.imread('IMG_9499')

# Load a pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Detect faces in the image
faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Ensure at least one face is detected
if len(faces) > 0:
    # Select the first detected face (you can modify this logic if needed)
    x, y, w, h = faces[0]

    # Crop the face region
    face_region = image[y:y+h, x:x+w]

    # Calculate the mean RGB value of the face region
    mean_rgb = np.mean(face_region, axis=(0, 1))
    
    # Convert the mean_rgb to integers
    mean_rgb = mean_rgb.astype(int)

    print(f"Mean RGB Value: R={mean_rgb[2]}, G={mean_rgb[1]}, B={mean_rgb[0]}")
else:
    print("No face detected in the image.")

# Display the cropped face region (optional)
cv2.imshow('Cropped Face', face_region)
cv2.waitKey(0)