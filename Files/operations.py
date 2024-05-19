import cv2 # Importing OpenCV library
import numpy as np  # Importing the NumPy library for array manipulation

# -------------------------------------Erosion-------------------------------------
def apply_erosion(image, kernel_size):
    """
    Apply erosion operation to the input image.

    Parameters:
        image (numpy.ndarray): Input image.
        kernel_size (int): Size of the kernel for erosion.

    Returns:
        numpy.ndarray: Image after erosion operation.
    """
    kernel = np.ones((kernel_size, kernel_size), np.uint8)  # Creating a square kernel of specified size
    return cv2.erode(image, kernel, iterations=1)  # Applying erosion to the image using the specified kernel

# -------------------------------------Dilation-------------------------------------
def apply_dilation(image, kernel_size):
    """
    Apply dilation operation to the input image.

    Parameters:
        image (numpy.ndarray): Input image.
        kernel_size (int): Size of the kernel for dilation.

    Returns:
        numpy.ndarray: Image after dilation operation.
    """
    kernel = np.ones((kernel_size, kernel_size), np.uint8)  # Creating a square kernel of specified size
    return cv2.dilate(image, kernel, iterations=1)  # Applying dilation to the image using the specified kernel

#-------------------------------------Opening-------------------------------------
def apply_opening(image, kernel_size):
    """
    Apply opening operation to the input image.

    Parameters:
        image (numpy.ndarray): Input image.
        kernel_size (int): Size of the kernel for opening.

    Returns:
        numpy.ndarray: Image after opening operation.
    """
    kernel = np.ones((kernel_size, kernel_size), np.uint8)  # Creating a square kernel of specified size
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)  # Applying opening operation to the image using the specified kernel

#-------------------------------------Closing-------------------------------------
def apply_closing(image, kernel_size):
    """
    Apply closing operation to the input image.

    Parameters:
        image (numpy.ndarray): Input image.
        kernel_size (int): Size of the kernel for closing.

    Returns:
        numpy.ndarray: Image after closing operation.
    """
    kernel = np.ones((kernel_size, kernel_size), np.uint8)  # Creating a square kernel of specified size
    return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)  # Applying closing operation to the image using the specified kernel
