# Image Processing

This project provides various image processing techniques implemented in Python using OpenCV. The tools include filtering, edge detection, morphological operations, segmentation, and Hough Transform for circle detection.

## Files and Functions

### 1. `filters.py`
This file contains functions for applying different filters to an image.

- **Low Pass Filter**: `apply_lpf(image, kernel_size)`
  - Applies a Gaussian blur to the image, effectively reducing high-frequency noise and details.
  - **Parameters**:
    - `image`: Input image.
    - `kernel_size`: Size of the kernel to be used for the filter (must be odd and positive).
  - **Returns**: Blurred image.

- **High Pass Filter**: `apply_hpf(image, kernel_size)`
  - Highlights high-frequency details in the image by subtracting a Gaussian-blurred version of the image from the original image.
  - **Parameters**:
    - `image`: Input image.
    - `kernel_size`: Size of the kernel to be used for the blur (must be odd and positive).
  - **Returns**: Image with high-pass filter applied.

- **Mean Filter**: `apply_mean_filter(image, kernel_size)`
  - Applies an averaging filter to the image, useful for reducing random noise.
  - **Parameters**:
    - `image`: Input image.
    - `kernel_size`: Size of the kernel to be used for the filter.
  - **Returns**: Image with mean filter applied.

- **Median Filter**: `apply_median_filter(image, kernel_size)`
  - Reduces noise in the image by replacing each pixel with the median of its neighborhood.
  - **Parameters**:
    - `image`: Input image.
    - `kernel_size`: Size of the kernel to be used for the filter (must be odd).
  - **Returns**: Image with median filter applied.

### 2. `edges.py`
This file contains functions for detecting edges using different techniques.

- **Roberts Edge Detection**: `apply_roberts_edge(image)`
  - Uses the Roberts cross operator to perform edge detection.
  - **Parameters**:
    - `image`: Input image.
  - **Returns**: Image with Roberts edge detection applied.

- **Prewitt Edge Detection**: `apply_prewitt_edge(image)`
  - Applies the Prewitt operator to detect edges by calculating the gradient of the image intensity.
  - **Parameters**:
    - `image`: Input image.
  - **Returns**: Image with Prewitt edge detection applied.

- **Sobel Edge Detection**: `apply_sobel_edge_detector(image)`
  - Detects edges using the Sobel operator, which calculates the gradient of the image intensity in the x and y directions.
  - **Parameters**:
    - `image`: Input image.
  - **Returns**: Image with Sobel edge detection applied.

### 3. `operations.py`
This file contains functions for morphological operations.

- **Erosion**: `apply_erosion(image, kernel_size)`
  - Erodes the boundaries of the foreground object.
  - **Parameters**:
    - `image`: Input image.
    - `kernel_size`: Size of the structuring element.
  - **Returns**: Image after erosion.

- **Dilation**: `apply_dilation(image, kernel_size)`
  - Dilates the boundaries of the foreground object.
  - **Parameters**:
    - `image`: Input image.
    - `kernel_size`: Size of the structuring element.
  - **Returns**: Image after dilation.

- **Opening**: `apply_opening(image, kernel_size)`
  - Applies an opening operation (erosion followed by dilation) to remove small objects.
  - **Parameters**:
    - `image`: Input image.
    - `kernel_size`: Size of the structuring element.
  - **Returns**: Image after opening.

- **Closing**: `apply_closing(image, kernel_size)`
  - Applies a closing operation (dilation followed by erosion) to close small holes.
  - **Parameters**:
    - `image`: Input image.
    - `kernel_size`: Size of the structuring element.
  - **Returns**: Image after closing.

### 4. `segmentation.py`
This file contains functions for image segmentation.

- **Region Split/Merge Segmentation**: `apply_region_split_merge_segmentation(photo)`
  - Segments the image by recursively splitting and merging regions.
  - **Parameters**:
    - `photo`: Input image.
  - **Returns**: Segmented image.

- **Thresholding**: `apply_thresholding(input_image, threshold_value=87, min_value=100, max_value=255)`
  - Applies thresholding to segment the image.
  - **Parameters**:
    - `input_image`: Input image.
    - `threshold_value`: Value to threshold the image.
    - `min_value`: Minimum value for thresholding.
    - `max_value`: Maximum value for thresholding.
  - **Returns**: Thresholded image.

### 5. `houghtransform.py`
This file contains the function for detecting circles using Hough Transform.

- **Hough Circle Transform**: `apply_hough_circle_transform(image)`
  - Detects circles in the image using the Hough Transform method.
  - **Parameters**:
    - `image`: Input image.
  - **Returns**: Image with detected circles highlighted.

### 6. `main.py`
This file contains the main program which uses Tkinter for a GUI to apply the above functions to images.

- **Load Image**: Opens a file dialog to load an image.
- **Show Original**: Displays the original image.
- **Apply Filter**: Applies a selected filter to the loaded image.

## How to Run

1. **Install Dependencies**:
   Make sure you have the necessary libraries installed. You can install them using pip:
   ```sh
   pip install opencv-python numpy matplotlib pillow

2. **Run the Main Program**:
    Execute the `main.py` file to start the application.
    ```sh
    python main.py

3. **Using the GUI**:
     - Click *Load Image* to open and display an image.
     - Use the other buttons to apply various filters and operations to the image.
     - Click *Show Original* to revert back to the original image.

4. **Example Usage**:

      - Load Image

      - Apply Low Pass Filter

      - Apply Sobel Edge Detector

      - Apply Hough Circle Transform