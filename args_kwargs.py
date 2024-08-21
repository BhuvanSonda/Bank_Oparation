import cv2
import numpy as np

# Load the image
image = cv2.imread('dog.jpg')

# Get the dimensions of the image
(h, w) = image.shape[:2]

# Define the center of the image
center = (w // 2, h // 2)

# Define the final rotation angle and scaling
final_angle = 180
scale = 1.0

# Number of steps for the animation
steps = 60  # More steps = smoother rotation

# Calculate the angle increment per step
angle_increment = final_angle / steps

# Loop to create the animation
for i in range(steps + 1):
    # Calculate the current angle
    angle = i * angle_increment
    
    # Get the rotation matrix for the current angle
    M = cv2.getRotationMatrix2D(center, angle, scale)
    
    # Rotate the image
    rotated_image = cv2.warpAffine(image, M, (w, h))
    
    # Display the rotated image
    cv2.imshow('Rotating Image', rotated_image)
    
    # Control the speed of rotation (delay in milliseconds)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

# Clean up
cv2.destroyAllWindows()
