import cv2
import numpy as np
from Convolution import convolution
from Gaussian_Blur import gaussian_blur


def Sobel_Gradient_Computation(image, kernel, debug=False):

    # Convolution of Image with Sobel Kernel in X-Axis
    image_xAxis = convolution(image, kernel, debug=debug)

    if debug:
        cv2.imshow('X Axis output', image_xAxis)
        cv2.waitKey(0)

    # Convolution of Image with Sobel Kernel in Y-Axis
    # Tranposed and Flipped the Sobel Kernel to Generate Kernel for Y-Axis
    image_yAxis = convolution(image, np.flip(kernel.T, axis=0), debug=debug)

    if debug:
        cv2.imshow('Y Axis output', image_yAxis)
        cv2.waitKey(0)

    # Final Computation of both Axis results
    # final Gradient = Sqrt( xAxis * xAxis + yAxis * yAxis)
    final_gradient = np.sqrt(np.square(image_xAxis) + np.square(image_yAxis))

    gradient_direction = np.arctan(image_yAxis / image_xAxis)

    # convert the Float64 data into Uint8 Data
    output = cv2.normalize(final_gradient, None, 255, 0,
                           cv2.NORM_MINMAX, cv2.CV_8UC1)

    direction = cv2.normalize(gradient_direction, None, 255, 0,
                              cv2.NORM_MINMAX, cv2.CV_8UC1)

    if debug:
        cv2.imshow('Gradient Direction output', direction)
        cv2.waitKey(0)

    if debug:
        cv2.imshow('Final Combined output', final_gradient)
        cv2.waitKey(0)

    return output


if __name__ == '__main__':
    image_path = r'C:\Users\suraj\Desktop\CV\Computation_Photography\Input_images\P1.jpg'
    image = cv2.imread(image_path)
    print(image.shape)

    # Parameters
    debug = False
    save = True
    resize = True
    kernel_size = 3
    kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    if resize:
        dsize = (image.shape[1]//7, image.shape[0]//7)
        input = cv2.resize(image, dsize)

    if not debug:
        cv2.imshow('input', input)
        cv2.waitKey(0)

    if save:
        cv2.imwrite(
            'Sobel_Gradient_Computation/Image_Outputs/Input.jpg', input)

    gb1 = gaussian_blur(input, kernel_size, debug)

    gb2 = gaussian_blur(input, 9, debug)

    output1 = Sobel_Gradient_Computation(gb1, kernel, False)

    output2 = Sobel_Gradient_Computation(gb2, kernel, False)

    if not debug:
        cv2.imshow('Sobel Edge detection1', output1)
        cv2.imshow('Sobel Edge detection2', output2)
        cv2.waitKey(0)

    if save:
        cv2.imwrite(
            'Sobel_Gradient_Computation/Image_Outputs/Sobel_Detection1.jpg', output1)
        cv2.imwrite(
            'Sobel_Gradient_Computation/Image_Outputs/Sobel_Detection2.jpg', output2)
