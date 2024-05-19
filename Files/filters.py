# Importing the OpenCV library
import cv2 

#-------------------------------------Low Pass Filter-------------------------------------
# Function to apply a low pass filter (Gaussian blur) to an image
def apply_lpf(image, kernel_size):
    # Apply GaussianBlur with the given kernel size and return the result
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

#-------------------------------------High Pass Filter-------------------------------------
# Function to apply a high pass filter to an image
def apply_hpf(image, kernel_size):
    # Convert the original image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur to the grayscale image with the selected kernel size
    blurred_image = cv2.GaussianBlur(gray_image, (kernel_size, kernel_size), 0)
    # Subtract the blurred image from the grayscale image to obtain the high-pass filtered image
    hpf_image = cv2.subtract(gray_image, blurred_image)
    # Convert the high-pass filtered image back to BGR format and return it
    return cv2.cvtColor(hpf_image, cv2.COLOR_GRAY2BGR)

#-------------------------------------Mean Filter-------------------------------------
# Function to apply a mean filter (simple blur) to an image
def apply_mean_filter(image, kernel_size):
    # Apply blur with the given kernel size and return the result
    return cv2.blur(image, (kernel_size, kernel_size))

#-------------------------------------Median Filter-------------------------------------
# Function to apply a median filter to an image
def apply_median_filter(image, kernel_size):
    # Apply medianBlur with the given kernel size and return the result
    return cv2.medianBlur(image, kernel_size)

