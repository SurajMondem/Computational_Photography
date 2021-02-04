import numpy as np
import cv2
import matplotlib.pyplot as plt


def convolution(image, kernel, average=False, debug=True):
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

    output_image = np.zeros(image.shape)

    pad_height = int((kernel_row - 1) / 2)
    pad_width = int((kernel_col - 1) / 2)

    padded_image = np.zeros(
        (image_row + (2 * pad_height), image_col + (2 * pad_width)))

    padded_image[pad_height: padded_image.shape[0] - pad_height,
                 pad_width: padded_image.shape[1] - pad_width] = image

    if debug:
        cv2.imshow("Padded Image", image)
        cv2.waitKey(0)

    for row in range(image_row):
        for col in range(image_col):
            output_image[row, col] = np.sum(
                kernel * padded_image[row: row + kernel_row, col: col + kernel_col])
            if average:
                output_image[row, col] //= kernel.shape[0] * kernel.shape[1]

    output = cv2.normalize(output_image, None, 255, 0,
                           cv2.NORM_MINMAX, cv2.CV_8UC1)
    cv2.imshow("Final test output", output)
    cv2.waitKey(0)

    return output_image
