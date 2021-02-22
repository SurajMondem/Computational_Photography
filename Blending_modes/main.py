import cv2
import numpy as np
from Divide import Divide
from Darken import Darken
from Lighten import Lighten
from Multiply import Multiply
from Screen import Screen
from Overlay import Overlay
from Addition import Addition
from Subtraction import Subtract
from Difference import Difference

if __name__ == '__main__':

    image1_path = r'C:\Users\suraj\Desktop\CV\Test_Images\DSC_0435_2.jpg'
    image2_path = r'C:\Users\suraj\Desktop\CV\Test_Images\DSC_0439_F.jpg'

    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    # parameters
    debug = False
    save = True
    resize = True
    ratio = 0.65

    # Convert image from 0-255 to 0-1
    img1 = img1 / 255
    img2 = img2 / 255

    if resize:
        dsize = (img1.shape[1]//2, img2.shape[0]//2)
        input1 = cv2.resize(img1, dsize)
        dsize = (img1.shape[1]//2, img2.shape[0]//2)
        input2 = cv2.resize(img2, dsize)

    if save:
        cv2.imwrite('Blending_modes/Outputs/Input1.jpg', input1 * 255)
        cv2.imwrite('Blending_modes/Outputs/Input2.jpg', input2 * 255)

    if not debug:
        cv2.imshow("input1 ", input1)
        cv2.imshow("input2 ", input2)
        cv2.waitKey(0)

    if ratio < 1:
        input1 = input1 * ratio
        input2 = input2 * (1 - ratio)

    imDivide = Divide(input1, input2, debug)
    imDarken = Darken(input1, input2, debug)
    imLighten = Lighten(input1, input2, debug)
    imMultiply = Multiply(input1, input2, debug)
    imScreen = Screen(input1, input2, debug)
    imOverlay = Overlay(input1, input2, debug)
    imAddition = Addition(input1, input2, debug)
    imSubtract = Subtract(input1, input2, debug)
    imDifference = Difference(input1, input2, debug)

    if not debug:
        cv2.imshow("Divide Output", imDivide)
        cv2.imshow("Darken Output", imDarken)
        cv2.imshow("Lighten Output", imLighten)
        cv2.imshow("Multiply Output", imMultiply)
        cv2.imshow("Screen Output", imScreen)
        cv2.imshow("Overlay Output", imOverlay)
        cv2.imshow("Addition Output", imAddition)
        cv2.imshow("Subtract Output", imSubtract)
        cv2.imshow("Difference Output", imDifference)
        cv2.waitKey(0)

    if save:
        cv2.imwrite("Blending_modes/Outputs/Divide.jpg", imDivide * 255)
        cv2.imwrite("Blending_modes/Outputs/Darken.jpg", imDarken * 255)
        cv2.imwrite("Blending_modes/Outputs/Lighten.jpg", imLighten * 255)
        cv2.imwrite("Blending_modes/Outputs/Multiply.jpg", imMultiply * 255)
        cv2.imwrite("Blending_modes/Outputs/Screen.jpg", imScreen * 255)
        cv2.imwrite("Blending_modes/Outputs/Overlay.jpg", imOverlay * 255)
        cv2.imwrite("Blending_modes/Outputs/Addition.jpg", imAddition * 255)
        cv2.imwrite("Blending_modes/Outputs/Subtract.jpg", imSubtract * 255)
        cv2.imwrite("Blending_modes/Outputs/Difference.jpg",
                    imDifference * 255)
