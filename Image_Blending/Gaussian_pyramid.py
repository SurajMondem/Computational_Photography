import numpy as np
import cv2
from Convolution import convolutionColor


def gaussian_pyramid(image, levels, debug=False):
    gpyramids = []
    gpyramids.append(image)
    temp = image
    print("total levels: ", levels)
    for i in range(1, levels):
        print("LEVEL NO. : ", i)
        temp = gaussian_reduce(temp, debug)
        gpyramids.append(temp)
        print("appended")

    return gpyramids


def gaussian_reduce(image, debug):
    output = None
    kernel = create_kernel(0.6, debug)
    print("convolution start")
    outputimage = convolutionColor(image, kernel, False, debug)
    print("convolution done")
    output = outputimage[::2, ::2, :]
    print("Resize done")
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
    save = False
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

    print(input.dtype)
    outputs = gaussian_pyramid(input, 5, debug)
    print(outputs[2].dtype)
    if not debug:
        a = 0
        for i in outputs:
            output = cv2.normalize(i, None, 255, 0,
                                   cv2.NORM_MINMAX, cv2.CV_8UC1)
            print(output.dtype)
            if save:
                cv2.imwrite(
                    'Image_Blending/Outputs/Gaussian_pyramid{}.jpg'.format(a), output)
            cv2.imshow('output {}'.format(a), output)
            a = a+1
        cv2.waitKey(0)
