import cv2
import numpy as np

class QuadNode:
    def __init__(self, x, y, w, h, data):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.data = data
        self.childs = []
        self.average = None  # To store average pixel value

class QuadTree:
    def __init__(self, image):
        self.root = QuadNode(0, 0, image.shape[1], image.shape[0], image)

    def calculate_average(self, node):
        """Calculates the average pixel value for the given node data."""
        if node.data.size > 0: 
            return np.mean(node.data)
        return 0

    def calculate_error(self, node, average):
        """Calculates the error based on how much pixel values differ from the average."""
        if node.data.size > 0:
            return np.mean((node.data - average) ** 2)
        return 0 

    def subdivide(self, node, threshold, min_size=2):
        """
        Subdivides the node if the error exceeds the threshold and size is above minimum.
        :param min_size: Minimum width/height of a node to allow subdivision.
        """
        if node.w <= min_size or node.h <= min_size:
            return

        average = self.calculate_average(node)
        node.average = average
        
        error = self.calculate_error(node, average)

        if error > threshold:  # Checking if the error exceeds the specified threshold
            half_w = node.w // 2
            half_h = node.h // 2

            # Ensure valid dimensions for subdivisions (handle odd-sized images).
            w1, h1 = half_w, half_h
            w2, h2 = node.w - half_w, node.h - half_h

            # Creating child nodes with adjusted boundaries
            child1 = QuadNode(node.x, node.y, w1, h1, node.data[:h1, :w1])  # Top-left
            child2 = QuadNode(node.x + w1, node.y, w2, h1, node.data[:h1, w1:])  # Top-right
            child3 = QuadNode(node.x, node.y + h1, w1, h2, node.data[h1:, :w1])  # Bottom-left
            child4 = QuadNode(node.x + w1, node.y + h1, w2, h2, node.data[h1:, w1:])  # Bottom-right
            
            # Appending the child nodes to the parent node's list
            node.childs.extend([child1, child2, child3, child4])

            # Recursively subdivide the child nodes
            for child in node.childs:
                self.subdivide(child, threshold, min_size)

    def build(self, threshold, min_size=2):
        """Builds the quad-tree based on the error threshold and minimum node size."""
        self.subdivide(self.root, threshold, min_size)

    def create_segmented_image(self, image_shape):
        """Creates a segmented image based on the quad-tree structure."""
        segmented_image = np.zeros(image_shape, dtype=np.uint8)
        self._fill_segmented_image(self.root, segmented_image)
        return segmented_image

    def _fill_segmented_image(self, node, segmented_image):
        """Recursively fill the segmented image based on the quad-tree nodes."""
        if node.average is not None:
            segmented_image[node.y:node.y + node.h, node.x:node.x + node.w] = int(node.average)

        for child in node.childs:
            self._fill_segmented_image(child, segmented_image)

    def visualize(self, image, node, depth=0):
        """Recursively draw the quad-tree on the image with enhanced visualization."""
        color_map = [
            (0, 255, 0),    # Depth 0 (green)
            (255, 0, 0),    # Depth 1 (red)
            (0, 0, 255),    # Depth 2 (blue)
            (255, 255, 0),  # Depth 3 (cyan)
            (255, 0, 255),  # Depth 4 (magenta)
            (0, 255, 255)   # Depth 5 (yellow)
        ]
        color = color_map[depth % len(color_map)]

        # Draw a rectangle around the current node
        cv2.rectangle(image, (node.x, node.y), (node.x + node.w, node.y + node.h), color, 1)

        # Add average pixel value text if valid
        if node.average is not None and not np.isnan(node.average):
            cv2.putText(image, f'{int(node.average)}', (node.x + 5, node.y + 15), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

        # Recursively draw for each child node
        for child in node.childs:
            self.visualize(image, child, depth + 1)

# Driver Code
if __name__ == "__main__":
    path = 'Your_Image.png'  # Paste image path here
    image = cv2.imread(path)
    if image is None:
        print("Image not found.")
    else:
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        quad_tree = QuadTree(grayscale_image)
        error_threshold = 50  # Adjust as needed
        min_node_size = 4  # Minimum size for subdivisions
        quad_tree.build(threshold=error_threshold, min_size=min_node_size)

        # Create a segmented image based on the quad-tree
        segmented_image = quad_tree.create_segmented_image(grayscale_image.shape)

        # Visualize the quad-tree by drawing rectangles on a copy of the grayscale image
        image_with_quadtree = cv2.cvtColor(grayscale_image, cv2.COLOR_GRAY2BGR)
        quad_tree.visualize(image_with_quadtree, quad_tree.root)

        # Display the images
        cv2.imshow("QuadTree Visualization", image_with_quadtree)
        cv2.imshow("Segmented Image", segmented_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
