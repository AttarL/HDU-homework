import cv2
img=cv2.imread("./ag.jpg")
gray_lap=cv2.Laplacian(img,cv2.CV_16S,ksize=3)
dst=cv2.convertScaleAbs(gray_lap)
cv2.imshow("a",dst)
cv2.waitKey(0)