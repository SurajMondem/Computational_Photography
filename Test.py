import numpy as np
import cv2


if __name__ == '__main__':

    # Read Image
    img = cv2.imread(r'C:\Users\suraj\Desktop\CV\Test_Images\lena1.jpg')

    print(img.shape)

    cv2.imshow('Input', img)

    row, col, color = img.shape

    for i in range(row):
        for j in range(col):
            for k in range(color):
                if img[i, j, k] != 0:
                    img[i, j, k] = 255
                else:
                    img[i, j, k] = 0

    # Write Image
    # cv2.imwrite('output.png', img)

    # Display Image
    cv2.imshow('Output', img)
    cv2.waitKey(0)
