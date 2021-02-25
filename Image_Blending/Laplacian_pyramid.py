import numpy as np
import cv2
from Convolution import convolutionColor
from Gaussian_pyramid import gaussian_pyramid


def laplacian_pyramid(gpyramids, debug=False):
    lpyramids = []
    k = len(gpyramids)
    print("total levels: ", k-1)
    for i in range(0, k-1):
        gu = gpyramids[i]
        egu = laplacian_expand(gpyramids[i+1])
        if egu.shape[0] > gu.shape[0]:
            egu = np.delete(egu, (-1), axis=0)
        if egu.shape[1] > gu.shape[1]:
            egu = np.delete(egu, (-1), axis=1)
        lpyramids.append(gu - egu)
    lpyramids.append(gpyramids.pop())
    return lpyramids


def laplacian_expand(image, debug=False):
    output = None
    kernel = create_kernel(0.4, debug)
    outimage = np.zeros(
        (image.shape[0]*2, image.shape[1]*2, image.shape[2]), dtype=np.float64)
    outimage[::2, ::2, :] = image[:, :, :]
    output = 4 * convolutionColor(outimage, kernel, False, debug)
    return output


def create_kernel(a, debug=False):
    kernel_Wx = np.array([[0.25 - a/2, 0.25, a, 0.25, 0.25 - a/2]])
    kernel = np.multiply(kernel_Wx, kernel_Wx.T)
    print("kernel created")
    if debug:
        print(kernel)

    return kernel


if __name__ == '__main__':
    path = r'C:\Users\suraj\Desktop\CV\Computation_Photography\Image_Blending\P1.jpg'
    image = cv2.imread(path)

    debug = False
    save = True
    resize = True

    row, col, color = image.shape
    max_pyramidx = int(np.log(row)/np.log(2) + 1)
    max_pyramidy = int(np.log(col)/np.log(2) + 1)
    levels = max_pyramidx if max_pyramidx <= max_pyramidy else max_pyramidy

    if resize:
        dsize = (image.shape[1]//5, image.shape[0]//5)
        input = cv2.resize(image, dsize)

    if not debug:
        cv2.imshow('input', input)
        if save:
            cv2.imwrite('Image_Blending/Outputs/Input.jpg', input)

    outputs = gaussian_pyramid(input, 5, debug)

    print(":::::LAPLACIAN COMPUTATION STARTS HERE:::::")

    laplacian_outputs = laplacian_pyramid(outputs)

    if not debug:
        a = 0
        k = len(laplacian_outputs)
        for i in range(k-1):
            output = cv2.normalize(laplacian_outputs[i], None, 255, 0,
                                   cv2.NORM_MINMAX, cv2.CV_8UC1)
            if save:
                cv2.imwrite(
                    'Image_Blending/Outputs/Laplacian_pyramid{}.jpg'.format(a), output)
            cv2.imshow('output {}'.format(a), output)
            a = a+1
        cv2.waitKey(0)
