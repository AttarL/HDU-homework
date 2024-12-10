import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('x-rayblog-gausian blur d4.jpg', cv2.IMREAD_GRAYSCALE)
kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])
fig, axs = plt.subplots(4, 1, figsize=(8, 10))
axs[0].imshow(image, cmap='gray')
axs[0].set_title('Original Image')
for i in range(3):
    sharpened_image = cv2.filter2D(image, -1, kernel)
    image = sharpened_image  # 更新图像为锐化后的图像
    axs[i + 1].imshow(sharpened_image, cmap='gray')
    axs[i + 1].set_title(f'Sharpened {i + 1} times')
    cv2.imwrite(f'sharpened_image_{i}.jpg', sharpened_image)
for ax in axs:
    ax.axis('off')
plt.tight_layout()
plt.savefig('1.jpg')
plt.show()
