import numpy as np
import cv2

# Read Image
img = cv2.imread('Works_images\Capture_img.JPG')

# Write Image
cv2.imwrite('output.png', img)

# Display Image
cv2.imshow('Output', img)
cv2.waitKey(0)
