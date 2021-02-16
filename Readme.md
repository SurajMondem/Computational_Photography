<h1 align="center">Computational Photography</h1>

<div align="center">
  :camera: :clipboard: :books: :clipboard: :camera:
</div>

<div align="center">
  <strong>Computational Photography Concepts implemented from scratch</strong>
</div>

<br />
## Table of Contents

- [x] [Kernel Convolutions](#features)
- [x] [Gaussian Blur](#example)
- [x] [Blending Modes](#philosophy)
- [x] [Sobel Gradient Computation](#events)
- [x] [Canny Edge Detector](#state)
- [ ] [Gaussian Pyramid](#routing)
- [ ] [Laplacian Pyramid](#server-rendering)
- [ ] [Merge Two Images](#components)

<br />

- ### Kernel Convolution

  The general expression of a convolution is

  ![Convolution](Assets\Convolution.svg)

  Depending on the element values, a kernel can cause a wide range of effects.
  <br/>

  **[Code](.\Kernel_Convolutions\Readme.md)**

<br />

- ### Gaussian Blur

  a Gaussian blur (also known as Gaussian smoothing) is the result of blurring an image by a Gaussian function

  The Gaussian blur is a type of image-blurring filters that uses a Gaussian function (which also expresses the normal distribution in statistics) for calculating the transformation to apply to each pixel in the image. The formula of a Gaussian function in one dimension is

  ![Convolution](Assets\Gaussian_blur.svg)
  <br/>

  **[Code](.\Kernel_Convolutions\Readme.md)**

- ### Blending Modes

  Blend modes in digital image editing and computer graphics are used to determine how two layers are blended with each other. The default blend mode in most applications is simply to obscure the lower layer by covering it with whatever is present in the top layer. However, as each pixel has a numerical representation, there exist a large number of ways to blend two layers.

  - **List of Blend Modes**
    1.  Addition
    2.  Darken
    3.  Difference
    4.  Divide
    5.  Lighten
    6.  Multiply
    7.  Overlay
    8.  Screen
    9.  Subtraction

    <br/>

  **[Code](.\Kernel_Convolutions\Readme.md)**
