import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./1.jpg',0)
def gamma_change(image, gamma):
    img_change = np.array(np.power(image/255, gamma)*255)
    return img_change
for i in range(1,10):
    g=i/4
    img_more = gamma_change(img, g)
    plt.subplot(3,3,i)
    plt.title("gamma = %.2f"%(g))
    plt.axis('off')
    plt.imshow(img_more, cmap="gray")
# gamma大于1，变亮;gamma小于1，变暗

plt.savefig('1_new.jpg')
plt.show()