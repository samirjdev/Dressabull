import cv2
import numpy as np

def extract_skin_color(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define a lower and upper range for detecting skin color in HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Create a mask to isolate the skin color
    skin_mask = cv2.inRange(hsv_image, lower_skin, upper_skin)

    # Bitwise AND the image with the skin mask
    skin_image = cv2.bitwise_and(image, image, mask=skin_mask)

    # Calculate the average skin color
    average_skin_color = np.mean(skin_image, axis=(0, 1))

    # Convert the average skin color to an RGB tuple
    average_skin_color_tuple = (int(average_skin_color[2]), int(average_skin_color[1]), int(average_skin_color[0]))

    return average_skin_color_tuple

if __name__ == "__main__":
    image_path = "/home/max/Downloads/PXL_20231022_194540734.jpg"  # Replace with the path to the photo
    skin_color = extract_skin_color(image_path)

    print(f"Average Skin Color (RGB Tuple): {skin_color}")


    import matplotlib.pyplot as plt

    # Define the RGB color (red in this example)
    rgb_color = skin_color  # Red in RGB format

    # Create a 1x1 pixel image with the specified color
    pixel = [[rgb_color]]

    # Display the pixel using Matplotlib
    plt.imshow(pixel)
    plt.axis('off')  # Turn off the axis labels
    plt.show()
