import cv2
import numpy as np
from Convolution import convolution
from Gaussian_Blur import gaussian_blur


def Sobel_edge_detection(image, kernel, debug=False):

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

    # convert the Float64 data into Uint8 Data
    output = cv2.normalize(final_gradient, None, 255, 0,
                           cv2.NORM_MINMAX, cv2.CV_8UC1)

    if debug:
        cv2.imshow('Final Combined output', final_gradient)
        cv2.waitKey(0)

    return output


if __name__ == '__main__':
    # Set Debug - True for Picture output after Every Step
    debug = False

    image_path = r'C:\Users\suraj\Desktop\CV\Computation_Photography\Input_images\P1.jpg'
    image = cv2.imread(image_path)
    print(image.shape)

    # Resize Large Picture to Small for Faster Processing
    image = cv2.resize(image, (image.shape[1]//5, image.shape[0]//5))

    if not debug:
        cv2.imshow('input', image)
        cv2.waitKey(0)

    # Sobel Kernel
    kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    image = gaussian_blur(image, 13, debug)
    if not debug:
        cv2.imshow('Gaussian blur output', image)
        cv2.waitKey(0)

    image = Sobel_edge_detection(image, kernel, False)
    if not debug:
        cv2.imshow('Sobel Edge detection', image)
        cv2.waitKey(0)
