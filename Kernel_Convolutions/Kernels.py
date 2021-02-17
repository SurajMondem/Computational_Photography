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

    # parameters
    # Color - True for color convolution
    # debug - Picture Display after every step
    color = True
    debug = False
    save = True
    resize = True

    if resize:
        # Resize the image
        dsize = (image.shape[1]//8, image.shape[0]//8)
        input = cv2.resize(image, dsize)

    if not debug:
        cv2.imshow('input', input)
        cv2.waitKey(0)

    if save:
        cv2.imwrite('Kernel_Convolutions/Outputs/Input.jpg', input)

    output1 = Identity_kernel(input, debug, color)
    if save:
        cv2.imwrite('Kernel_Convolutions/Outputs/Identity.jpg', output1)

    output2 = Highpass_kernel(input, debug, color)
    if save:
        cv2.imwrite('Kernel_Convolutions/Outputs/HighPass.jpg', output2)

    output3 = Sharpen_kernel(input, debug, color)
    if save:
        cv2.imwrite('Kernel_Convolutions/Outputs/Sharpen.jpg', output3)

    output4 = Emboss_kernel(input, debug, color)
    if save:
        cv2.imwrite('Kernel_Convolutions/Outputs/Emboss.jpg', output4)

    output5 = Box_blur(input, debug, color)
    if save:
        cv2.imwrite('Kernel_Convolutions/Outputs/BoxBlur.jpg', output5)
