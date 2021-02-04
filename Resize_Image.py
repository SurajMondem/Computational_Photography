import numpy as num
import cv2
from PIL import Image


img = cv2.imread('.\Input_images\P1.jpg')
print(img.shape)

dsize = (img.shape[1] // 5, img.shape[0] // 5)  # (width, height)

# resize image
output = cv2.resize(img, dsize)
print(output.shape)

cv2.imwrite('./Output_images/Resize_output6.jpg', output)
