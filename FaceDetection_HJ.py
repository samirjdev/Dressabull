import cv2

# Load the Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load an image
image = cv2.imread('Test_Image2.jpg')

# Convert the image to grayscale for better detection
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Create a folder to save the cropped faces (if it doesn't exist)
import os
if not os.path.exists('cropped_faces'):
    os.mkdir('cropped_faces')

# Counter for naming the cropped face images
face_count = 0

# Process only the first detected face (if any)
if len(faces) > 0:
    x, y, w, h = faces[0]  # Get the coordinates of the first detected face
    face = image[y:y + h, x:x + w]
    cv2.imwrite(f'cropped_faces/face_{face_count}.jpg', face)
    
    # Draw a rectangle around the first detected face
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    face_count += 1

# Display the image with the detected face(s)
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
