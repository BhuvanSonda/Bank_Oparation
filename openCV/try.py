# import numpy as np
# import cv2 as cv

# # Create an image of 100x100 pixels with the color [197, 197, 197]
# color = np.zeros((100, 100, 3), dtype=np.uint8)
# color[:] = [77 ,77 ,77]



# # Display the image
# while True:

#     cv.imshow('Gray Color', color)
#     key = cv.waitKey(1) & 0xFF
#     print(key)
#     # Check if the 'q' key was pressed
#     if key == ord('q'):
#         print("You pressed 'q'. Exiting...",key,ord('q'))
#         break
# cv.destroyAllWindows()



import cv2

# Load a color image
#color_image = cv2.imread("C:\\Users\\Docketrun\\Pictures\\Screenshots\\images.jpg")
color_image = cv2.imread("""C:\\Users\Docketrun\Pictures\Screenshots\images.jpg""")

# Convert the color image to grayscale
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# Access a specific pixel
color_pixel = color_image[10, 100]  # BGR values at position (100, 100)
gray_pixel = gray_image[10, 100]    # Grayscale value at position (100, 100)

print(f"Color Pixel: {color_pixel}")
print(f"Grayscale Pixel : {gray_pixel}")
