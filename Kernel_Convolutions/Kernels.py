import cv2
import numpy as np
from Convolution import convolution
from Convolution import convolutionColor


def Identity_kernel(image, debug=False, color=False):
    # Nothing Simply copy the image
    kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])

    if color:
        return convolutionColor(image, kernel, average=False, debug=debug)
    else:
        return convolution(image, kernel, average=False, debug=debug)


def Highpass_kernel(image, debug=False, color=False):
    # Finds the edges
    kernel1 = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    kernel2 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

    if color:
        return convolutionColor(image, kernel1, average=False, debug=debug)
    else:
        return convolution(image, kernel1, average=False, debug=debug)


def Sharpen_kernel(image, debug=False, color=False):
    # sharpens the image
    kernel = np.array([[-1, -1, -1], [-1, 11, -1], [-1, -1, -1]])

    if color:
        return convolutionColor(image, kernel, average=False, debug=debug)
    else:
        return convolution(image, kernel, average=False, debug=debug)


def Emboss_kernel(image, debug=False, color=False):
    # Lifts the non edge parts - emboss it to stand out
    kernel = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])

    if color:
        return convolutionColor(image, kernel, average=False, debug=debug)
    else:
        return convolution(image, kernel, average=False, debug=debug)


def Box_blur(image, debug=False, color=False):
    # plain blur the image
    kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    if color:
        return convolutionColor(image, kernel, average=True, debug=debug)
    else:
        return convolution(image, kernel, average=True, debug=debug)


if __name__ == '__main__':
    image_path = r'C:\Users\suraj\Desktop\CV\Computation_Photography\Input_images\P1.jpg'
    image = cv2.imread(image_path)

    # Resize the image
    dsize = (image.shape[1]//5, image.shape[0]//5)
    input = cv2.resize(image, dsize)

    # parametes
    # Color - True for color convolution
    # debug - Picture Display after every step
    color = True
    debug = False

    if not debug:
        cv2.imshow('input', input)
        cv2.waitKey(0)

    Identity_kernel(input, debug, color)

    Highpass_kernel(input, debug, color)

    Sharpen_kernel(input, debug, color)

    Emboss_kernel(input, debug, color)

    Box_blur(input, debug, color)
