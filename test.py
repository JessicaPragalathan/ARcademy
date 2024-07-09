import cv2

# Load an image
image = cv2.imread('Images\Snare.png')

# Check if the image was loaded successfully
if image is None:
    print("Error: Unable to load image.")
else:
    # Display the image in a window
    cv2.imshow('Image', image)
    
    # Wait for a key press
    cv2.waitKey(0)
    
    # Close all OpenCV windows
    cv2.destroyAllWindows()
