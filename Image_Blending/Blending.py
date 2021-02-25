import numpy as np
import cv2
import math
from Convolution import convolutionColor
from Gaussian_pyramid import gaussian_pyramid
from Laplacian_pyramid import laplacian_pyramid
from Laplacian_pyramid import laplacian_expand


def blend(lapl_white_img, lapl_black_img, gauss_mask_img):
    blended_pyramid = []
    k = len(gauss_mask_img)
    for i in range(0, k):
        p1 = gauss_mask_img[i] * lapl_white_img[i]
        p2 = (1 - gauss_mask_img[i]) * lapl_black_img[i]
        blended_pyramid.append(p1 + p2)
    return blended_pyramid


def collapse(output_pyramid):
    output = None
    output = np.zeros(
        (output_pyramid[0].shape[0], output_pyramid[0].shape[1], output_pyramid[0].shape[2]), dtype=np.float64)
    for i in range(len(output_pyramid)-1, 0, -1):
        lap = laplacian_expand(output_pyramid[i])
        lapb = output_pyramid[i-1]
        if lap.shape[0] > lapb.shape[0]:
            lap = np.delete(lap, (-1), axis=0)
        if lap.shape[1] > lapb.shape[1]:
            lap = np.delete(lap, (-1), axis=1)
        tmp = lap + lapb
        output_pyramid.pop()
        output_pyramid.pop()
        output_pyramid.append(tmp)
        output = tmp
    return output


if __name__ == '__main__':

    debug = False
    save = False

    path = 'Image_Blending/Assets/Input_images/'
    image1 = cv2.imread(path + 'Stars_small.jpg')
    image2 = cv2.imread(path + 'Road1_small.jpg')
    mask = cv2.imread(path + 'Gradient1_small.png')

    print(image1.shape)
    print(image2.shape)
    print(mask.shape)

    min_size = min(image1.shape[0], image1.shape[1])
    # at least 16x16 at the highest level.
    depth = int(math.floor(math.log(min_size, 2))) - 4

    print(depth)
    print(min_size)

    print("::::: STEP 1 ::::::")
    gaussian_img1 = gaussian_pyramid(image1, depth)
    print("::::: STEP 2 ::::::")
    gaussian_img2 = gaussian_pyramid(image2, depth)
    print("::::: STEP 3 ::::::")
    gaussian_mask = gaussian_pyramid(mask, depth)
    for x in range(len(gaussian_mask)):
        gaussian_mask[x] = gaussian_mask[x] / 255
    print("::::: STEP 4 ::::::")
    laplacian_img1 = laplacian_pyramid(gaussian_img1)
    print("::::: STEP 5 ::::::")
    laplacian_img2 = laplacian_pyramid(gaussian_img2)

    print("::::: STEP 6 ::::::")
    output_pyramid = blend(laplacian_img2, laplacian_img1, gaussian_mask)

    print("::::: STEP 7 ::::::")
    output_collapse = collapse(output_pyramid)
    output_collapse[output_collapse < 0] = 0
    output_collapse[output_collapse > 255] = 255

    print("::::: DONE :::::")
    if not debug:
        a = 0
        output1 = cv2.normalize(
            output_collapse, None, 255, 0, cv2.NORM_MINMAX, cv2.CV_8UC1)
        cv2.imshow('image1 {}'.format(a), output1)
        a = a+1
        cv2.waitKey(0)
