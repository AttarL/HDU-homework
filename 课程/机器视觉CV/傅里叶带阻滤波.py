#带阻滤波

import numpy as np
import matplotlib.pyplot as plt
import cv2


def band_reject_filter(image, freq_low, freq_high):
    # 傅立叶变换
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)

    # 获取频率域图像的尺寸
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2

    # 创建带阻滤波器掩模
    mask = np.ones((rows, cols), np.uint8)

    # 计算中心点到各个位置的距离，构建带阻滤波器
    for i in range(rows):
        for j in range(cols):
            dist = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)
            if freq_low <= dist <= freq_high:
                mask[i, j] = 0

    # 应用滤波器掩模
    fshift_filtered = fshift * mask

    # 傅立叶逆变换，得到滤波后的图像
    f_ishift = np.fft.ifftshift(fshift_filtered)
    image_filtered = np.fft.ifft2(f_ishift)
    image_filtered = np.abs(image_filtered)
    image_filtered = np.uint8(image_filtered)

    return image_filtered


# 读取图像
image = cv2.imread('1-2.png', cv2.IMREAD_GRAYSCALE)

# 设定带阻滤波器的频率范围（单位：像素）
freq_low = 20  # 低频
freq_high = 35  # 高频

# 应用带阻滤波器
filtered_image = band_reject_filter(image, freq_low, freq_high)

# 显示滤波后的图像
plt.figure(figsize=(6, 6))
plt.imshow(filtered_image, cmap='gray')
plt.title(' ({}-{} Hz)'.format(freq_low, freq_high))
plt.axis('off')
plt.show()
