import numpy as np
import cv2
import math
from Convolution import convolution


def gaussian_blur(image, kernel_size, debug=False):
    kernel = create_Kernel(
        kernel_size, sigma=math.sqrt(kernel_size), debug=debug)
    return convolution(image, kernel, average=True, debug=debug)


def create_Kernel(size, sigma=4, debug=False):
    kernel_1D = np.linspace(-(size // 2), size // 2, size)
    for i in range(size):
        kernel_1D[i] = dnorm(kernel_1D[i], 0, sigma)
    kernel_2D = np.outer(kernel_1D.T, kernel_1D.T)

    kernel_2D *= 1.0 / kernel_2D.max()

    if debug:
        cv2.imshow("Kernel ( {}X{} )".format(size, size), kernel_2D)
        cv2.waitKey(0)

    return kernel_2D


def dnorm(x, mu, sd):
    return 1 / (np.sqrt(2 * np.pi) * sd) * np.e ** (-np.power((x - mu) / sd, 2) / 2)


if __name__ == '__main__':
    path = r'C:\Users\suraj\Desktop\CV\Computation_Photography\Gaussian_Blur\P1.jpg'
    image = cv2.imread(path)

    print(image.shape)
    dsize = (image.shape[1]//5, image.shape[0]//5)
    input = cv2.resize(image, dsize)

    print(input.shape)
    kernel_size = 3
    debug = False

    gaussian_blur(input, kernel_size, debug)
