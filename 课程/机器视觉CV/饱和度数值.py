import cv2
import numpy as np

# 读取图像
image = cv2.imread('image1.bmp')  # 替换为你的图像文件路径

# 将图像转换到HSV空间
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 提取饱和度分量
saturation_channel = hsv_image[:, :, 1]  # 从HSV图像中获取饱和度分量（索引为1）

# 查看像素饱和度值
height, width = saturation_channel.shape[:2]
for y in range(height):
    for x in range(width):
        saturation_value = saturation_channel[y, x]
        print(f"Pixel at ({x}, {y}) - Saturation: {saturation_value}")

# 或者，你也可以直接输出整个饱和度分量矩阵
print("Saturation Channel Matrix:")
print(saturation_channel)
