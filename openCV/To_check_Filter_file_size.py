import cv2
import os

image = cv2.imread('openCV/cat.jpg',0)

gaussian_blur = cv2.GaussianBlur(image, (15, 15),5)

bilateral_filter = cv2.bilateralFilter(image, 10, 175, 175)

cv2.imwrite('gaussian_blur.jpg', gaussian_blur)
cv2.imwrite('bilateral_filter.jpg', bilateral_filter)

cv2.imshow('gaussian_blur.jpg', gaussian_blur)
cv2.imshow('bilateral_filter.jpg', bilateral_filter)
cv2.waitKey(0)
cv2.destroyAllWindows()

original_size = os.path.getsize('openCV/cat.jpg')
print(f"Original Image Size: {original_size} bytes")

gaussian_size = os.path.getsize('gaussian_blur.jpg')
print(f"Gaussian Blur Image Size: {gaussian_size} bytes")

bilateral_size = os.path.getsize('bilateral_filter.jpg')
print(f"Bilateral Filter Image Size: {bilateral_size} bytes")


