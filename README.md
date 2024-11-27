# **Image Segmentation using Quad Tree Method**

This project implements the Quad Tree method for image segmentation. The algorithm recursively divides an image into quadrants based on an error threshold, simplifying and segmenting the image into regions of similar pixel intensity. The project also includes visualization of the Quad Tree structure on the image.

---

## **Features**

- **Dynamic Error Threshold**: Control the segmentation quality by adjusting the error threshold.
- **Handles Odd-Sized Images**: Robust to images with non-divisible dimensions.
- **Visualization**: Visualizes the Quad Tree structure with depth-based color coding.
- **Customizable Minimum Node Size**: Prevents unnecessary subdivisions for very small regions.
- **Grayscale Segmentation**: Simplifies color images into grayscale for efficient processing.

---

## **Requirements**

Make sure you have the following installed:

- **Python 3.7+**
- **OpenCV**: `pip install opencv-python`
- **NumPy**: `pip install numpy`

---

## **Usage**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/quad-tree-image-segmentation.git
   cd quad-tree-image-segmentation
2. Replace the image path in the script (path variable) with your desired image.

3. Run the script:
   ```bash
   python quad_tree_segmentation.py
3. Adjust the error threshold and minimum node size for your desired segmentation output:

  - **error_threshold**: Controls segmentation sensitivity.
  - **min_node_size**: Sets the smallest allowable quadrant size.
## **Output**
The program displays two results:

1. **Quad Tree Visualization**: A color-coded visualization of the Quad Tree structure on the image.
     
2. **Segmented Image**: The image segmented into regions based on pixel intensity similarity.
   
   <img width="605" alt="image" src="https://github.com/user-attachments/assets/4064d8e4-a34e-4bdd-bfbc-18b35c0f0ecd">

## **Code Explanation**
### **Quad Tree Structure**
The Quad Tree divides the image into quadrants recursively based on:

- **Error Threshold**: The variance of pixel intensities within a quadrant.
- **Minimum Size**: Prevents splitting quadrants below a certain size.
### **Key Functions**
- **calculate_average(node)**: Computes the average pixel value of a quadrant.
- **calculate_error(node, average)**: Calculates the error based on the average pixel intensity.
- **subdivide(node, threshold, min_size)**: Recursively divides a quadrant if the error exceeds the threshold.
- **visualize(image, node, depth)**: Draws the Quad Tree structure with color-coded depths.
- **create_segmented_image(image_shape)**: Generates the segmented image from the Quad Tree.
## **Visualization Example**
Here’s an example of the output for an image:

- **Quad Tree Visualization**
   ![image](https://github.com/user-attachments/assets/af200fd4-4f70-4f16-a793-c9367d9168c9)
- **Segmented Image**
 <img width="605" alt="image" src="https://github.com/user-attachments/assets/4064d8e4-a34e-4bdd-bfbc-18b35c0f0ecd">

## **Customization**
- **Threshold Adjustment**:
Modify the ```error_threshold```  value in the script to change the sensitivity of the segmentation. A lower value results in more detailed segmentation.

- **Minimum Node Size**:
Change ```min_node_size``` to control the smallest allowable quadrant size.

## **Future Enhancements**
- **Support for color image segmentation**.
- **Optimizations for larger images**.
- **Interactive GUI for real-time threshold adjustment**.
## **Contributing**
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.
