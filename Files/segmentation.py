import cv2  # Importing the OpenCV library for image processing

# -------------------------------------apply_region_split_merge_segmentation-------------------------------------
def apply_region_split_merge_segmentation(photo):
    """
    Apply region split and merge segmentation to the input image.

    Parameters:
        photo (numpy.ndarray): Input image.

    Returns:
        numpy.ndarray: Image after region split and merge segmentation.
    """
    # Convert the input image to grayscale
    image = cv2.cvtColor(photo, cv2.COLOR_RGB2GRAY)
    region_split_merge_image = image.copy()  # Create a copy of the grayscale image
    height, width = region_split_merge_image.shape[:2]  # Get the dimensions of the image

    # Function for region growing
    def region_growing(image, seed):
        visited = set()  # Set to store visited pixels
        stack = [seed]  # Stack to store pixels to be processed

        while stack:
            x, y = stack.pop()  # Pop a pixel from the stack
            if (x, y) not in visited:
                visited.add((x, y))  # Mark the pixel as visited
                # Check neighboring pixels
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        nx, ny = x + dx, y + dy
                        # Check if the neighboring pixel is within the image bounds
                        if 0 <= nx < width and 0 <= ny < height:
                            # Check the intensity difference between the current pixel and its neighbor
                            if abs(int(image[y, x]) - int(image[ny, nx])) < 20:
                                stack.append((nx, ny))  # Add the neighboring pixel to the stack

        return visited  # Return the set of visited pixels

    # Function to merge regions
    def merge_regions(visited_regions):
        new_regions = []  # List to store merged regions
        for region in visited_regions:
            merged_region = region.copy()  # Copy the current region
            while True:
                for other_region in visited_regions:
                    # Check if there's an intersection between the current region and other regions
                    if other_region != region and not set(region).isdisjoint(other_region):
                        merged_region.update(other_region)  # Merge the regions
                        visited_regions.remove(other_region)  # Remove the merged region from the list
                        break
                else:
                    break
            new_regions.append(merged_region)  # Add the merged region to the list
        return new_regions  # Return the list of merged regions

    seeds = [(0, 0), (width - 1, 0), (0, height - 1), (width - 1, height - 1)]  # Seeds for region growing

    visited_regions = []  # List to store visited regions
    for seed in seeds:
        visited_region = region_growing(region_split_merge_image, seed)  # Apply region growing
        visited_regions.append(visited_region)  # Add the visited region to the list

    merged_regions = merge_regions(visited_regions)  # Merge the visited regions

    for region in merged_regions:
        for x, y in region:
            region_split_merge_image[y, x] = 255  # Set the pixel intensity to 255 for the merged region

    return region_split_merge_image  # Return the image after region split and merge segmentation


# -------------------------------------Segmentation using Thresholding-------------------------------------
def apply_thresholding(input_image, threshold_value=87, min_value=10, max_value=255):
    """
    Apply segmentation using thresholding to the input image.

    Parameters:
        input_image (numpy.ndarray): Input image.
        threshold_value (int): Threshold value for segmentation (default is 87).
        min_value (int): Minimum value for thresholding (default is 100).
        max_value (int): Maximum value for thresholding (default is 255).

    Returns:
        numpy.ndarray: Segmented image.
    """
    # Convert the input image to grayscale
    gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, threshold = cv2.threshold(
        gray_image, threshold_value, max_value, cv2.THRESH_BINARY)

    # Set pixels below the minimum value to the minimum value
    threshold[threshold < min_value] = min_value

    return threshold  # Return the segmented image
