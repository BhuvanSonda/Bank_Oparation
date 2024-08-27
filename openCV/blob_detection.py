import cv2
import numpy as np

# Initialize parameters for blob detection
params = cv2.SimpleBlobDetector_Params()
print(params)
# Set parameters 
params.filterByArea = True#Only blobs with a certain area are considered
params.minArea = 100#Sets the minimum area for a blob to be detected
params.filterByCircularity = False#the blob detection process will not consider the shape of the blobs when detecting them.
params.filterByConvexity = False
#params.minConvexity = .5
params.filterByInertia = False

# Create a blob detector with the specified parameters
detector = cv2.SimpleBlobDetector_create(params)

# Load an image in grayscale
img = cv2.imread('dog.jpg',0)

# Detect blobs
keypoints = detector.detect(img)

# Draw detected blobs as red circles
img_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255),
                                       cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


# Show the detecting area on the image
cv2.imshow('Blob Detection', img_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
