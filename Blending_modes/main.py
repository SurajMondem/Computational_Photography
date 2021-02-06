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

    print(img1.shape)
    print(img2.shape)

    img1 = img1 / 255
    img2 = img2 / 255

    cv2.imshow("input1 ", img1)
    cv2.imshow("input2 ", img2)
    cv2.waitKey(0)

    imDivide = Divide(img1, img2, False)
    imDarken = Darken(img1, img2, False)
    imLighten = Lighten(img1, img2, False)
    imMultiply = Multiply(img1, img1, False)
    imScreen = Screen(img1, img2, False)
    imOverlay = Overlay(img1, img2, False)
    imAddition = Addition(img1, img2, False)
    imSubtract = Subtract(img1, img2, False)
    imDifference = Difference(img1, img2, False)

    imDivide = cv2.resize(
        imDivide, (imDivide.shape[1]//3, imDivide.shape[0]//3))
    imDarken = cv2.resize(
        imDarken, (imDarken.shape[1]//3, imDarken.shape[0]//3))
    imLighten = cv2.resize(
        imLighten, (imLighten.shape[1]//3, imLighten.shape[0]//3))
    imMultiply = cv2.resize(
        imMultiply, (imMultiply.shape[1]//3, imMultiply.shape[0]//3))
    imScreen = cv2.resize(
        imScreen, (imScreen.shape[1]//3, imScreen.shape[0]//3))
    imOverlay = cv2.resize(
        imOverlay, (imOverlay.shape[1]//3, imOverlay.shape[0]//3))
    imAddition = cv2.resize(
        imAddition, (imAddition.shape[1]//3, imAddition.shape[0]//3))
    imSubtract = cv2.resize(
        imSubtract, (imSubtract.shape[1]//3, imSubtract.shape[0]//3))
    imDifference = cv2.resize(
        imDifference, (imDifference.shape[1]//3, imDifference.shape[0]//3))

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
