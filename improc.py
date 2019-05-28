import cv2
import matplotlib.pyplot as plt
import numpy as np

# Shorthand function for binarizing an imge with a given threshold value.
def binarize(img, threshold=80):
    _, img = cv2.threshold(img,threshold,255,cv2.THRESH_BINARY)
    return img

# Convolve image with a kernel
def convolve(img, kernel):
    return cv2.filter2D(img, -1, kernel)

# Converts uint8 images to float images, leaves float32 images untouched
def as_float_img(img):
    if img.dtype == np.dtype('uint8'):
        return img.astype(np.float32) / 255
    return img

# Converts float32 images to uint8 images, leaves uint8 images untouched
def as_int_img(img):
    if img.dtype == np.dtype('float32'):
        return (img * 255).astype(np.uint8)
    return img