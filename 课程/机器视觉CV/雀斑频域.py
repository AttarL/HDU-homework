import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('2.png', 0)
f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)
rows, cols = image.shape
crow, ccol = rows//2 , cols//2
mask = np.zeros((rows, cols), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1
fshift = fshift * mask
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)  # (5, 5)是高斯核的大小，0是标准差
mean_blur = cv2.blur(image, (5, 5))  # (5, 5)是滤波器的大小

cv2.imshow('Original Image', image)
cv2.imshow('Frequency Domain Filtered Image', np.uint8(img_back))
cv2.imwrite('FD.png', img_back)
cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.imshow('Mean Blur', mean_blur)
cv2.imwrite('GB.png', gaussian_blur)
cv2.imwrite('MB.png', mean_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
