import cv2
import numpy as np

# 读取彩色图像
image = cv2.imread('sunflower.jpg')  # 替换为你的图像文件路径

# 将图像转换到 HSV 颜色空间
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 定义蓝色的颜色阈值范围
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([120, 255, 255])

# 定义白色的颜色阈值范围
lower_white = np.array([0, 0, 200])
upper_white = np.array([180, 30, 255])

# 创建蓝色的掩码
blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

# 创建白色的掩码
white_mask = cv2.inRange(hsv_image, lower_white, upper_white)

# 合并掩码
unwanted_mask = cv2.bitwise_or(blue_mask, white_mask)

# 使用腐蚀和膨胀操作进一步处理掩码
kernel = np.ones((5, 5), np.uint8)
unwanted_mask = cv2.morphologyEx(unwanted_mask, cv2.MORPH_OPEN, kernel)

# 应用掩码到原始图像上
filtered_image = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(unwanted_mask))

# 显示原始图像和处理后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.imwrite('filtered_image.jpg', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
