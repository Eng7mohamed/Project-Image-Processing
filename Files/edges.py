# Importing the OpenCV library
import cv2

# Importing the NumPy library
import numpy as np

# -------------------------------------Edge Detection (Roberts)-------------------------------------
# Function to apply Roberts edge detection (using Canny edge detector here)
def apply_roberts_edge(image):
    # Apply the Canny edge detector with thresholds 100 and 200
    return cv2.Canny(image, 100, 200)

# -------------------------------------Edge Detection (Prewitt)-------------------------------------
# Function to apply Prewitt edge detection
def apply_prewitt_edge(image):
    # Define the Prewitt kernel for the x direction
    kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    # Define the Prewitt kernel for the y direction
    kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    # Apply the Prewitt kernel in the x direction
    img_prewittx = cv2.filter2D(image, -1, kernelx)
    # Apply the Prewitt kernel in the y direction
    img_prewitty = cv2.filter2D(image, -1, kernely)
    # Combine the results of Prewitt x and y using addWeighted
    return cv2.addWeighted(img_prewittx, 0.5, img_prewitty, 0.5, 0)

# -------------------------------------Edge Detection (Sobel)-------------------------------------
# Function to apply Sobel edge detection
def apply_sobel_edge_detector(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Sobel edge detection in the x direction
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    # Apply Sobel edge detection in the y direction
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

    # Combine the results of Sobel x and y using addWeighted
    sobel_combined = cv2.addWeighted(cv2.convertScaleAbs(
        sobel_x), 0.5, cv2.convertScaleAbs(sobel_y), 0.5, 0)

    # Return the combined Sobel edge detected image
    return sobel_combined
