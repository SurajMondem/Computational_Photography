import numpy as np
import cv2
import matplotlib.pyplot as plt


def convolutionColor(image, kernel, average=False, debug=True):
    # Color Convolution of the Image with kernel
    # Implements 3*3 kernel on all 3 layers(RGB) of the images

    print("Image Shape : {}".format(image.shape))
    print("Kernel shape : {}".format(kernel.shape))

    if debug:
        cv2.imshow('Image', image)
        cv2.waitKey(0)

    image_row, image_col, image_c = image.shape
    kernel_row, kernel_col = kernel.shape

    # Sample matrix of size of image
    output_image = np.zeros(image.shape)

    # calculate the required padding according to kernel size
    pad_height = int((kernel_row - 1) / 2)
    pad_width = int((kernel_col - 1) / 2)
    pad_color = 3

    # create sample image with padding
    padded_image = np.full(
        (image_row + (2 * pad_height), image_col + (2 * pad_width), image_c), (0, 0, 0))

    # insert the image into the padded image
    padded_image[pad_height: image_row + pad_height,
                 pad_width: image_col + pad_width] = image

    if debug:
        cv2.imshow("Padded Image", image)
        cv2.waitKey(0)

    # Convolute the padded image with the given kernel
    for color in range(image_c):
        for row in range(image_row):
            for col in range(image_col):
                output_image[row, col, color] = np.sum(
                    kernel * padded_image[row: row + kernel_row, col: col + kernel_col, color])
                if average:
                    output_image[row, col,
                                 color] //= kernel.shape[0] * kernel.shape[1]

    # convert the Float64 data into Uint8 Data
    output = cv2.normalize(output_image, None, 255, 0,
                           cv2.NORM_MINMAX, cv2.CV_8UC1)

    # Display the Final output
    cv2.imshow("Final test output", output)
    cv2.waitKey(0)

    return output_image


def convolution(image, kernel, average=False, debug=True):
    # Checks if the image is RGB
    # if Yes then converts it into grayscale
    if len(image.shape) == 3:
        print("Found 3 channels : {}".format(image.shape))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print("Converted to Gray Channel. size : {}".format(image.shape))
    else:
        print("Image Shape : {}".format(image.shape))

    print("Kernel shape : {}".format(kernel.shape))

    if debug:
        cv2.imshow('Image', image)
        cv2.waitKey(0)

    image_row, image_col = image.shape
    kernel_row, kernel_col = kernel.shape

    # Sample matrix of size of image
    output_image = np.zeros(image.shape)

    # calculate the required padding according to kernel size
    pad_height = int((kernel_row - 1) / 2)
    pad_width = int((kernel_col - 1) / 2)

    # create sample image with padding
    padded_image = np.zeros(
        (image_row + (2 * pad_height), image_col + (2 * pad_width)))

    print(padded_image.dtype)

    # insert the image into the padded image
    padded_image[pad_height: padded_image.shape[0] - pad_height,
                 pad_width: padded_image.shape[1] - pad_width] = image

    if debug:
        cv2.imshow("Padded Image", image)
        cv2.waitKey(0)

    # Convolute the padded image with the given kernel
    for row in range(image_row):
        for col in range(image_col):
            output_image[row, col] = np.sum(
                kernel * padded_image[row: row + kernel_row, col: col + kernel_col])
            if average:
                output_image[row, col] //= kernel.shape[0] * kernel.shape[1]

    print(output_image.dtype)
    # convert the Float64 data into Uint8 Data
    output = cv2.normalize(output_image, None, 255, 0,
                           cv2.NORM_MINMAX, cv2.CV_8UC1)

    # Display the Final output
    cv2.imshow("Final test output", output_image)
    cv2.waitKey(0)

    return output_image
