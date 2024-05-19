# Importing necessary libraries
from turtle import bgcolor  # Importing bgcolor from turtle module
import cv2  # Importing OpenCV library
import matplotlib.pyplot as plt  # Importing matplotlib's pyplot module
import numpy as np  # Importing NumPy library
from glob import glob  # Importing glob module for file manipulation
import tkinter as tk  # Importing tkinter for GUI
from tkinter import filedialog  # Importing filedialog from tkinter for file selection dialog
from PIL import Image, ImageTk  # Importing Image and ImageTk from PIL for image processing

# Importing custom modules/files
import filters  # Importing filters.py module
import edges  # Importing edges.py module
import operations  # Importing operations.py module
import segmentation  # Importing segmentation.py module
import houghtransform  # Importing houghtransform.py module

# ------------------------------------- Main -------------------------------------

# Function to open an image file and display it in a new window
def load_image():
    global img, original_img, photo, image_window
    file_path = filedialog.askopenfilename()  # Open file dialog to select an image
    if file_path:  # If a file is selected
        img = cv2.cvtColor(cv2.imread(file_path), cv2.COLOR_BGR2RGB)  # Read image in RGB format
        original_img = img.copy()  # Store the original image
        photo = ImageTk.PhotoImage(image=Image.fromarray(img))  # Create a PhotoImage object
        if 'image_window' in globals():
            image_window.destroy()  # If image window exists, destroy it
        image_window = tk.Toplevel(root)  # Create a new image window
        image_window.title("Loaded Image")  # Set window title
        canvas = tk.Canvas(image_window, width=img.shape[1], height=img.shape[0], background="black")  # Create canvas
        canvas.create_image(0, 0, image=photo, anchor=tk.NW)  # Display image on canvas
        canvas.pack()

# Function to show the original image
def show_original_image():
    global original_img, photo, image_window
    photo = ImageTk.PhotoImage(image=Image.fromarray(original_img))  # Create PhotoImage object from original image
    if 'image_window' in globals():
        image_window.destroy()  # If image window exists, destroy it
    image_window = tk.Toplevel(root)  # Create a new image window
    image_window.title("Original Image")  # Set window title
    canvas = tk.Canvas(image_window, width=original_img.shape[1], height=original_img.shape[0])  # Create canvas
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)  # Display image on canvas
    canvas.pack()

# Function to apply a filter and update the image in the new window
def apply_filter(filter_func, *args):
    global img, photo, image_window
    processed_img = filter_func(img, *args)  # Apply filter function to image
    photo = ImageTk.PhotoImage(image=Image.fromarray(processed_img))  # Create PhotoImage object from processed image
    if 'image_window' in globals():
        image_window.destroy()  # If image window exists, destroy it
    image_window = tk.Toplevel(root)  # Create a new image window
    image_window.title("Processed Image")  # Set window title
    image_window.resizable(False, False)  # Make the window fixed size
    canvas = tk.Canvas(image_window, width=processed_img.shape[1], height=processed_img.shape[0])  # Create canvas
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)  # Display image on canvas
    canvas.pack()

# Initialize the main window
root = tk.Tk()  # Create Tkinter root window
root.title("Image Processing Tools")  # Set window title

# Function to create a button in the main window
def create_button(window, row, column, text, command):
    button = tk.Button(window, text=text, command=command, bg="purple", fg="white")  # Create button
    button.grid(row=row, column=column, padx=5, pady=5)  # Add button to grid layout

# Create buttons for filters and operations
create_button(root, 0, 0, "Load Image", load_image)  # Button to load image
create_button(root, 0, 1, "Show Original", show_original_image)  # Button to show original image
create_button(root, 0, 2, "Low Pass Filter", lambda: apply_filter(filters.apply_lpf, 25))  # Button for Low Pass Filter
create_button(root, 1, 0, "High Pass Filter", lambda: apply_filter(filters.apply_hpf, 25))  # Button for High Pass Filter
create_button(root, 1,1, "Mean Filter", lambda: apply_filter(filters.apply_mean_filter, 5))  # Button for Mean Filter
create_button(root, 1, 2, "Median Filter", lambda: apply_filter(filters.apply_median_filter, 5))  # Button for Median Filter
create_button(root, 2, 0, "Roberts Edge", lambda: apply_filter(edges.apply_roberts_edge))  # Button for Roberts Edge
create_button(root, 2, 1, "Prewitt Edge", lambda: apply_filter(edges.apply_prewitt_edge))  # Button for Prewitt Edge
create_button(root, 2, 2, "Sobel Edge Detector", lambda: apply_filter(edges.apply_sobel_edge_detector))  # Button for Sobel Edge Detector
create_button(root, 3, 0, "Erosion", lambda: apply_filter(operations.apply_erosion, 5))  # Button for Erosion
create_button(root, 3, 1, "Dilation", lambda: apply_filter(operations.apply_dilation, 5))  # Button for Dilation
create_button(root, 3, 2, "Opening", lambda: apply_filter(operations.apply_opening, 5))  # Button for Opening
create_button(root, 4, 0, "Closing", lambda: apply_filter(operations.apply_closing, 5))  # Button for Closing
create_button(root, 4, 1, "Region Split/Merge Segmentation", lambda: apply_filter(segmentation.apply_region_split_merge_segmentation))  # Button for Region Split/Merge Segmentation
create_button(root, 4, 2, "Thresholding", lambda: apply_filter(segmentation.apply_thresholding))  # Button for Thresholding
create_button(root, 5, 1, "Hough Circle Transform", lambda: apply_filter(houghtransform.apply_hough_circle_transform))  # Button for Hough Circle Transform

# Run the main loop
root.mainloop()  # Start the Tkinter event loop
