import cv2
import numpy as np


def homomorphic_filtering(image_path, alpha=0.8, beta=1.2):
    # 读取图像
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # 转换图像为浮点类型
    img_float = np.float32(img) / 255.0

    # 将图像转换到对数域
    img_log = np.log1p(img_float)

    # 应用傅里叶变换
    img_fft = np.fft.fft2(img_log)
    img_fft_shift = np.fft.fftshift(img_fft)

    # 构建同态滤波器
    rows, cols, _ = img.shape
    crow, ccol = rows // 2, cols // 2
    D = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            D[i, j] = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)

    H = (beta - alpha) * (1 - np.exp(-0.5 * (D ** 2 / (30 ** 2)))) + alpha

    # 进行频域滤波
    img_fft_shift_filtered = img_fft_shift * H[:, :, np.newaxis]
    img_fft_filtered = np.fft.ifftshift(img_fft_shift_filtered)
    img_filtered = np.fft.ifft2(img_fft_filtered)
    img_filtered = np.exp(np.real(img_filtered)) - 1

    # 将结果转换回图像格式
    img_filtered = np.clip(img_filtered, 0, 1)
    img_filtered = np.uint8(img_filtered * 255)

    return img_filtered


# 调用同态滤波函数来增强黑暗山洞图片的细节
input_image = '3.jpg'
output_image = homomorphic_filtering(input_image)

# 显示原始图片和增强后的图片
original_img = cv2.imread(input_image, cv2.IMREAD_COLOR)
cv2.imwrite('ttlb.jpg', output_image)
cv2.imshow('Original Image', original_img)
cv2.imshow('Enhanced Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
