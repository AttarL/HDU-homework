import cv2
import numpy as np

# 读取彩色图像
image = cv2.imread('sunflower.jpg')  # 替换为你的彩色图像文件路径

# 将图像转换到 HSV 颜色空间
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# 向日葵花瓣的颜色阈值范围（黄色）
lower_yellow = np.array([0, 100, 100])
upper_yellow = np.array([40, 255, 255])

# 向日葵中心的颜色阈值范围（绿色和黄色交接）
lower_green_yellow = np.array([0, 0, 50])
upper_green_yellow = np.array([40, 255, 255])
# 创建向日葵花瓣的掩码
petal_mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

# 创建向日葵中心的掩码
center_mask = cv2.inRange(hsv_image, lower_green_yellow, upper_green_yellow)
# 合并两个掩码
combined_mask = cv2.bitwise_or(petal_mask, center_mask)
# 应用掩码到原始图像上
segmented_image = cv2.bitwise_and(image, image, mask=combined_mask)
# 显示原始图像和分割后的向日葵图像

# 获取屏幕的分辨率
screen_width, screen_height = 1080, 1080  # 替换为你的屏幕分辨率

# 计算图像缩放比例
scale_factor = min(screen_width / image.shape[1], screen_height / image.shape[0])

# 缩放图像
scaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)
# 创建窗口并显示图像
cv2.namedWindow('Segmented Sunflower', cv2.WINDOW_NORMAL)  # 创建可调整大小的窗口
# 自适应窗口大小
cv2.imshow('Segmented Sunflower', segmented_image)
cv2.resizeWindow('Segmented Sunflower', (int(image.shape[1]*scale_factor), int(image.shape[0]*scale_factor)))
cv2.imwrite('sunfloweronly.jpg', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
