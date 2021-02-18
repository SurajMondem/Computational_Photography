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
    return convolution(image, kernel, average=True, debug=debug)


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


if __name__ == '__main__':
    path = r'C:\Users\suraj\Desktop\CV\Computation_Photography\Gaussian_Blur\P1.jpg'
    image = cv2.imread(path)

    debug = False
    save = True
    resize = True
    kernel_size = 3

    if resize:
        dsize = (image.shape[1]//7, image.shape[0]//7)
        input = cv2.resize(image, dsize)

    if not debug:
        cv2.imshow('input', input)
        cv2.waitKey(0)

    if save:
        cv2.imwrite('Gaussian_Blur/Outputs/Input.jpg', input)

    output1 = gaussian_blur(input, kernel_size, debug)

    if not debug:
        cv2.imshow('input', output1)
        cv2.waitKey(0)

    if save:
        cv2.imwrite('Gaussian_Blur/Outputs/Gaussian_blur1.jpg', output1)

    output2 = gaussian_blur(input, 9, debug)

    if not debug:
        cv2.imshow('input', output2)
        cv2.waitKey(0)

    if save:
        cv2.imwrite('Gaussian_Blur/Outputs/Gaussian_blur2.jpg', output2)
