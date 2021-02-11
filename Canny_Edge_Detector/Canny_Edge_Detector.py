import numpy as np
import cv2
from Gaussian_Blur import gaussian_blur
from Sobel_detection import Sobel_Gradient_Computation

import matplotlib.pyplot as plt


def Non_Maximum_Suppression(mag, dir, debug=False):
    image_row, image_col = mag.shape
    output = np.zeros(mag.shape)
    PI = 180

    for row in range(1, image_row - 1):
        for col in range(1, image_col - 1):
            direction = dir[row, col]

            if (0 <= direction < PI/8) or (15*PI/8 < direction <= 16*PI/8):
                before = mag[row, col - 1]
                after = mag[row, col + 1]
            elif (PI/8 <= direction < 3*PI/8) or (9*PI/8 < direction <= 11*PI/8):
                before = mag[row + 1, col - 1]
                after = mag[row - 1, col+1]
            elif (3*PI/8 <= direction < 5*PI/8) or (11*PI/8 < direction <= 13*PI/8):
                before = mag[row - 1, col]
                after = mag[row + 1, col]
            else:
                before = mag[row - 1, col - 1]
                after = mag[row + 1, col + 1]

            if (mag[row, col] >= before) and (mag[row, col] >= after):
                output[row, col] = mag[row, col]

    if debug:
        cv2.imshow('Non Maximum Supression', output)
        cv2.waitKey(0)

    return output


def threshold(image, low, high, weak, strong, debug=False):
    threshold_output = np.zeros(image.shape)

    strong_row, strong_col = np.where(image >= high)
    weak_row, weak_col = np.where((image <= high) & (image >= low))

    threshold_output[strong_row, strong_col] = strong
    threshold_output[weak_row, weak_col] = weak

    if debug:
        outputT = cv2.normalize(src=threshold_output, dst=None, alpha=0,
                                beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

        cv2.imshow('Thresholding Output', outputT)
        cv2.waitKey(0)

    return threshold_output


def hysteresis(image, weak):
    image_row, image_col = image.shape

    top_to_bottom = image.copy()

    for row in range(1, image_row):
        for col in range(1, image_col):
            if top_to_bottom[row, col] == weak:
                if top_to_bottom[row, col + 1] == 255 or top_to_bottom[row, col - 1] == 255 or top_to_bottom[row - 1, col] == 255 or top_to_bottom[
                        row + 1, col] == 255 or top_to_bottom[
                        row - 1, col - 1] == 255 or top_to_bottom[row + 1, col - 1] == 255 or top_to_bottom[row - 1, col + 1] == 255 or top_to_bottom[
                        row + 1, col + 1] == 255:
                    top_to_bottom[row, col] = 255
                else:
                    top_to_bottom[row, col] = 0

    bottom_to_top = image.copy()

    for row in range(image_row - 1, 0, -1):
        for col in range(image_col - 1, 0, -1):
            if bottom_to_top[row, col] == weak:
                if bottom_to_top[row, col + 1] == 255 or bottom_to_top[row, col - 1] == 255 or bottom_to_top[row - 1, col] == 255 or bottom_to_top[
                        row + 1, col] == 255 or bottom_to_top[
                        row - 1, col - 1] == 255 or bottom_to_top[row + 1, col - 1] == 255 or bottom_to_top[row - 1, col + 1] == 255 or bottom_to_top[
                        row + 1, col + 1] == 255:
                    bottom_to_top[row, col] = 255
                else:
                    bottom_to_top[row, col] = 0

    right_to_left = image.copy()

    for row in range(1, image_row):
        for col in range(image_col - 1, 0, -1):
            if right_to_left[row, col] == weak:
                if right_to_left[row, col + 1] == 255 or right_to_left[row, col - 1] == 255 or right_to_left[row - 1, col] == 255 or right_to_left[
                        row + 1, col] == 255 or right_to_left[
                        row - 1, col - 1] == 255 or right_to_left[row + 1, col - 1] == 255 or right_to_left[row - 1, col + 1] == 255 or right_to_left[
                        row + 1, col + 1] == 255:
                    right_to_left[row, col] = 255
                else:
                    right_to_left[row, col] = 0

    left_to_right = image.copy()

    for row in range(image_row - 1, 0, -1):
        for col in range(1, image_col):
            if left_to_right[row, col] == weak:
                if left_to_right[row, col + 1] == 255 or left_to_right[row, col - 1] == 255 or left_to_right[row - 1, col] == 255 or left_to_right[
                        row + 1, col] == 255 or left_to_right[
                        row - 1, col - 1] == 255 or left_to_right[row + 1, col - 1] == 255 or left_to_right[row - 1, col + 1] == 255 or left_to_right[
                        row + 1, col + 1] == 255:
                    left_to_right[row, col] = 255
                else:
                    left_to_right[row, col] = 0

    final_image = top_to_bottom + bottom_to_top + right_to_left + left_to_right

    final_image[final_image > 255] = 255

    return final_image


if __name__ == '__main__':
    # compute Canny Edge Detector
    image_path = r'C:\Users\suraj\Desktop\CV\Computation_Photography\Input_images\P1.jpg'
    image = cv2.imread(image_path)
    print(image.shape)
    resize = True

    # Resize Large Picture to Small for Faster Processing
    if resize:
        image = cv2.resize(image, (image.shape[1]//5, image.shape[0]//5))

    # Set debug - True for pictures of every step
    debug = False
    if not debug:
        cv2.imshow('input', image)
        cv2.waitKey(0)

    # Step 1: Smoothing
    blur_output = gaussian_blur(image, 9, debug)
    if not debug:
        # convert the Float64 data into Uint8 Data
        output1 = cv2.normalize(src=blur_output, dst=None, alpha=0,
                                beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

        cv2.imshow('Gaussian Blur Output', output1)
        cv2.waitKey(0)

    # Step 2: Compute Magnitude and Orientation of Gradient
    kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  # Sobel Kernel

    magnitude, orientation = Sobel_Gradient_Computation(
        blur_output, kernel, True, debug)

    if not debug:
        output2 = cv2.normalize(src=magnitude, dst=None, alpha=0,
                                beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

        cv2.imshow('Sobel Gradient Computation', output2)
        cv2.waitKey(0)

    # Step 3: Non-Maximum Suppression
    NMS_result = Non_Maximum_Suppression(magnitude, orientation, debug)
    if not debug:
        output3 = cv2.normalize(src=NMS_result, dst=None, alpha=0,
                                beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        cv2.imshow('Non Maximum Suppression', output3)
        cv2.waitKey(0)

    # Step 4: Linking and Thresholding (hysteresis)
    # Step 4.1: Thresholding
    weak = 50
    strong = 255
    thres = threshold(NMS_result, 5, 20, weak=weak, strong=strong, debug=debug)

    if not debug:
        outputT = cv2.normalize(src=thres, dst=None, alpha=0,
                                beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

        cv2.imshow('Thresholding Output', outputT)
        cv2.waitKey(0)

    # Step 4.2: Hysteresis
    final_image = hysteresis(thres, weak)

    if not debug:
        final_output = cv2.normalize(src=final_image, dst=None, alpha=0,
                                     beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

        cv2.imshow('Canny Edge Detection Output', final_output)
        cv2.waitKey(0)
