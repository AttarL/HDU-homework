import cv2
import numpy as np

# 灰度化
def BGR2GRAY(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()
    gray_img = 0.2126 * r + 0.7152 * g + 0.0722 * b
    gray_img = gray_img.astype(np.uint8)
    return gray_img


# 大津二值化算法
def otsu(gray_img):
    h = gray_img.shape[0]
    w = gray_img.shape[1]
    threshold_t = 0
    max_g = 0
    # 遍历每一个灰度层
    for t in range(255):
        # 使用numpy直接对数组进行计算
        n0 = gray_img[np.where(gray_img < t)]
        n1 = gray_img[np.where(gray_img >= t)]
        w0 = len(n0) / (h * w)
        w1 = len(n1) / (h * w)
        u0 = np.mean(n0) if len(n0) > 0 else 0
        u1 = np.mean(n1) if len(n1) > 0 else 0

        g = w0 * w1 * (u0 - u1) ** 2
        if g > max_g:
            max_g = g
            threshold_t = t
    print('类间方差最大阈值：', threshold_t)
    gray_img[gray_img < threshold_t] = 0
    gray_img[gray_img > threshold_t] = 255
    return gray_img


# 这里直接将数据转换成float32了，方便后续计算
img=cv2.imread("./gk.jpg").astype(np.float32)
gray_img = BGR2GRAY(img)
otsu_img = otsu(gray_img)
cv2.imshow('otsu_img', otsu_img)
cv2.waitKey(0)  # 等待3000ms=3s
cv2.destroyAllWindows()