# Importing the OpenCV library
import cv2
# Importing the NumPy library
import numpy as np

# Function to apply Hough Transform for detecting circles in an image
def apply_hough_circle_transform(image):
    # Convert to grayscale if input is a 3-channel image (BGR)
    if len(image.shape) == 3 and image.shape[2] == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Use input image as grayscale if it's already 2-channel or grayscale
    elif len(image.shape) == 2 or (len(image.shape) == 3 and image.shape[2] == 1):
        gray_image = image
    else:
        raise ValueError("Unsupported number of channels in the input image")

    # Detect circles using Hough circle transform with specified parameters
    circles = cv2.HoughCircles(gray_image, cv2.HOUGH_GRADIENT, dp=1, minDist=300, param1=50, param2=30, minRadius=0, maxRadius=0)

    # If circles are detected, draw them on a copy of the original image and return
    if circles is not None:
        circles = np.uint16(np.around(circles))  # Convert circle parameters to integer
        hough_image = image.copy()  # Create a copy of the original image
        for i in circles[0, :]: # type: ignore
            # Draw outer circle
            cv2.circle(hough_image, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # Draw center of the circle
            cv2.circle(hough_image, (i[0], i[1]), 2, (0, 0, 255), 3)
        return hough_image  # Return the image with detected circles drawn
    else:
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Return the original image if no circles are detected
