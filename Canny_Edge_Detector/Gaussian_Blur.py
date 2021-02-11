import numpy as np
import cv2
import math
from Convolution import convolution


def gaussian_blur(image, kernel_size, debug=False):

    # Create kernel of the following values
    # size - kernel_size
    # standard Deviation - root of kernel_size for quick data (works for data 3-21)
    kernel = create_Kernel(
        kernel_size, sigma=math.sqrt(kernel_size), debug=debug)

    # return the convoluted the data passing the kernel
    blur = convolution(image, kernel, average=True, debug=debug)

    if debug:
        # convert the Float64 data into Uint8 Data
        output = cv2.normalize(blur, None, 255, 0,
                               cv2.NORM_MINMAX, cv2.CV_8UC1)
        cv2.imshow('Gradient Direction output', output)
        cv2.waitKey(0)

    return blur


def create_Kernel(size, sigma=1, debug=False):

    # Create Equal spaced matrix
    kernel_1D = np.linspace(-(size // 2), size // 2, size)

    # Normalize the elements of the Matrix
    for i in range(size):
        kernel_1D[i] = dnorm(kernel_1D[i], 0, sigma)

    # convert the 1D matrix to size * size 2D matrix
    kernel_2D = np.outer(kernel_1D.T, kernel_1D.T)

    # making center element value to 1 respective to all the elements
    kernel_2D *= 1.0 / kernel_2D.max()

    if debug:
        cv2.imshow("Kernel ( {}X{} )".format(size, size), kernel_2D)
        cv2.waitKey(0)

    return kernel_2D


def dnorm(x, mu, sd):
    # Univariate normal distribution formulae
    # sd - Standard Deviation
    # mu - Mean
    # x - Data
    return (1 / (np.sqrt(2 * np.pi) * sd)) * np.e ** (-np.power((x - mu) / sd, 2) / 2)
