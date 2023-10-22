import cv2
import numpy as np

def skin_color_analysis(image_path):
    # Check if the image path exists
    image = None
    valid_extensions = ('.jpg', '.jpeg', '.png')

    for ext in valid_extensions:
        full_path = image_path + ext
        if cv2.haveImageReader(full_path):
            image = cv2.imread(full_path)
            break

    if image is None:
        print("Error: Could not read the image or unsupported image format.")
        return
    
    # Calculate the new window size (half the height and width) while preserving aspect ratio
    height, width, _ = image.shape
    new_height = height // 8
    new_width = width // 7

    # Convert the image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define a range for skin color in HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Create a mask that identifies skin color in the image
    skin_mask = cv2.inRange(hsv_image, lower_skin, upper_skin)

    # Apply the mask to the original image
    skin_detected = cv2.bitwise_and(image, image, mask=skin_mask)

    # Get the average color of the skin
    skin_color = np.mean(skin_detected, axis=(0, 1))

    # Extract the RGB values
    red_component = int(skin_color[2])
    green_component = int(skin_color[1])
    blue_component = int(skin_color[0])

    # Set the window size to the new dimensions
    cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Skin Detected', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Original Image', new_width, new_height)
    cv2.resizeWindow('Skin Detected', new_width, new_height)

    # Display the original image and the skin-detected image
    cv2.imshow('Original Image', image)
    cv2.imshow('Skin Detected', skin_detected)

    print(f"RGB Components: ({red_component}, {green_component}, {blue_component})")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "image"  # Replace with the base name of your image (without the extension)
    skin_color_analysis(image_path)