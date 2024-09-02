import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("temple_run.jpg", 0)
colored_img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
ret, binary = cv.threshold(img, 100, 255, cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(colored_img, contours, -1, (0, 0, 255), 2)

plt.subplot()
plt.imshow(colored_img)
plt.title('Original Image with Contours')
plt.axis('off')

cv.imshow("Contours", colored_img)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
