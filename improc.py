import cv2
import matplotlib.pyplot as plt
import numpy as np
import filesys as fs

""" IMAGE TYPES """
# Returns true if image is of type float
def is_float_img(img):
    return img.dtype == np.dtype('float32')

# Returns true if image is of type int
def is_int_img(img):
    img.dtype == np.dtype('uint8')

# Converts uint8 images to float images, leaves float32 images untouched
def as_float_img(img):
    if is_int_img(img):
        return img.astype(np.float32) / 255
    return img

# Converts float32 images to uint8 images, leaves uint8 images untouched
def as_int_img(img):
    if is_float_img(img):
        return (img * 255).astype(np.uint8)
    return img

""" READING / SHOWING / WRITING """
# Shows image for certain amount of seconds
def timshow(img, seconds=0):
    fig = plt.figure()
    plt.imshow(img)
    if seconds > 0:
        plt.show(block=False)
        plt.pause(seconds)
        plt.close()
        return
    plt.show()

# Read image into desired format, default=float
def imread(filename, astype=float):
    im = plt.imread(filename)
    if (astype == int):
        return as_int_img(im)
    if (astype == float):
        return as_float_img(im)
    return None

def imwrite(filename, create_directories=False):
    if create_directories:
        fs.create_dirs_if_not_exist(os.path.dirname(filename))
    # TODO:::::


""" IMAGE EDITTING """
# Shorthand function for binarizing an imge with a given threshold value.
# Threshold is always float, in case of int: threshold is multiplied by 255
def binarize(img, threshold=0.3):
    if is_int_img(img):
        _, img = cv2.threshold(img,int(threshold * 255),255,cv2.THRESH_BINARY)
    else:
        _, img = cv2.threshold(img,threshold,1.0,cv2.THRESH_BINARY)
    return img

# Convolve image with a kernel
def convolve(img, kernel):
    return cv2.filter2D(img, -1, kernel)

# Apply blur
def blur (img, intensity=4):
    d = int(intensity)
    kernel = np.ones((d,d),np.float32)/(d*d)
    return cv2.filter2D(img,-1,kernel)