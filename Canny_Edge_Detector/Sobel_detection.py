import cv2
import numpy as np
from Convolution import convolution


def Sobel_Gradient_Computation(image, kernel, convert_to_degree=False, debug=False):

    # Convolution of Image with Sobel Kernel in X-Axis
    image_xAxis = convolution(image, kernel, debug=debug)

    if debug:
        image1 = cv2.normalize(src=image_xAxis, dst=None, alpha=0,
                               beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        cv2.imshow('X Axis output', image1)
        cv2.waitKey(0)

    # Convolution of Image with Sobel Kernel in Y-Axis
    # Tranposed and Flipped the Sobel Kernel to Generate Kernel for Y-Axis
    image_yAxis = convolution(image, np.flip(kernel.T, axis=0), debug=debug)

    if debug:
        image2 = cv2.normalize(src=image_yAxis, dst=None, alpha=0,
                               beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        cv2.imshow('Y Axis output', image2)
        cv2.waitKey(0)

    # Final Computation of both Axis results
    # final Gradient = Sqrt( xAxis * xAxis + yAxis * yAxis)
    final_gradient = np.sqrt(np.square(image_xAxis) + np.square(image_yAxis))

    # Gradient Orientation
    # Orientation direction = arcTan (YAxis / XAxis)
    gradient_direction = np.arctan2(image_yAxis, image_xAxis)

    if convert_to_degree:
        gradient_direction = np.rad2deg(gradient_direction)
        gradient_direction += 180

    if debug:
        final_gradient = cv2.normalize(src=final_gradient, dst=None, alpha=0,
                                       beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        cv2.imshow('Final Combined output', final_gradient)
        cv2.waitKey(0)

    return final_gradient, gradient_direction
