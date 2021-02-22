import cv2
import numpy as np


def Overlay(image1, image2, debug=False):
    if debug:
        cv2.imshow('Image1', image1)
        cv2.imshow('Image2', image2)
        cv2.waitKey(0)

    image1_row, image1_col, image1_color = image1.shape
    image2_row, image2_col, image2_color = image2.shape

    output_image = np.zeros(image1.shape)

    for col in range(len(image1)):
        for row in range(len(image1[col])):
            for color in range(len(image1[col][row])):
                if image1[col][row][color] < 0.5:
                    if 2 * image2[col][row][color] * image1[col][row][color] > 1:
                        output_image[col][row][color] = 1
                    else:
                        output_image[col][row][color] = 2 * image2[col][row][color] * \
                            image1[col][row][color]
                else:
                    if 1 - 2 * (1 - image2[col][row][color]) * (1 - image1[col][row][color]) < 0:
                        output_image[col][row][color] = 0
                    elif 1 - 2 * (1 - image2[col][row][color]) * (1 - image1[col][row][color]) > 1:
                        output_image[col][row][color] = 1
                    else:
                        output_image[col][row][color] = 1 - 2 * \
                            (1 - image2[col][row][color]) * \
                            (1 - image1[col][row][color])

    print(output_image)

    # Display the Final output
    if debug:
        cv2.imshow("Final test output", output_image)
        cv2.waitKey(0)

    return output_image
