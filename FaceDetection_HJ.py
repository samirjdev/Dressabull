import cv2

# Load the Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load an image
image = cv2.imread('Test_Image1.jpeg')

# Convert the image to grayscale for better detection
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Create a folder to save the cropped faces (if it doesn't exist)
#import os
#if not os.path.exists('cropped_faces'):
    #os.mkdir('cropped_faces')

# Initialize variables to keep track of the largest face
largest_area = 0
largest_face = None

# Iterate through the detected faces to find the largest one
for (x, y, w, h) in faces:
    face = image[y:y + h, x:x + w]
    face_area = w * h
    
    if face_area > largest_area:
        largest_area = face_area
        largest_face = face

# Save the largest face
if largest_face is not None:
    cv2.imwrite('largest_face.jpg', largest_face)
    
    # Draw a rectangle around the largest detected face
    x, y, w, h = faces[0]
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with the largest detected face
#cv2.imshow('Face Detection', image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
