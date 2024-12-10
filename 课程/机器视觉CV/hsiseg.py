#h
import cv2
import numpy as np

# 读取图像
image = cv2.imread('image1.bmp')

# 将图像转换到HSI空间
hsi_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 获取H分量（色调）
h_channel = hsi_image[:, :, 0].astype(np.float32)

# 定义一个25x25的算术平均掩模
kernel_size = 25
kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size * kernel_size)

# 对H分量进行平滑处理（使用滤波器）
smoothed_h = cv2.filter2D(h_channel, -1, kernel)

# 将处理后的H分量放回HSI图像
hsi_image_smoothed = hsi_image.copy()
hsi_image_smoothed[:, :, 0] = smoothed_h.astype(np.uint8)

# 将处理后的HSI图像转换回RGB空间
smoothed_rgb_image = cv2.cvtColor(hsi_image_smoothed, cv2.COLOR_HSV2BGR)
cv2.imwrite('smoothed_h.jpg', smoothed_rgb_image)
# 显示原始图像和处理后的图像
cv2.imshow('Smoothed Image', smoothed_rgb_image)
#s

# 获取S分量（饱和度）
s_channel = hsi_image[:, :, 1].astype(np.float32)

# 定义一个25x25的算术平均掩模
kernel_size = 25
kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size * kernel_size)

# 对S分量进行平滑处理（使用滤波器）
smoothed_s = cv2.filter2D(s_channel, -1, kernel)

# 将处理后的S分量放回HSI图像
hsi_image_s = hsi_image.copy()
hsi_image_s[:, :, 1] = smoothed_s.astype(np.uint8)

# 将处理后的HSI图像转换回RGB空间
smoothed_s_image = cv2.cvtColor(hsi_image_s, cv2.COLOR_HSV2BGR)

# 显示原始图像和处理后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Smoothed_S', smoothed_s_image)
cv2.imwrite('smoothed_s.jpg', smoothed_s_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
