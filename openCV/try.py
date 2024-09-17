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


import pandas as pd
import os

class Update:
    @staticmethod
    def AC_entry(name, account_no, sign, init_balance, mobile_no, adhar_no, time, ac_type, accounts_file):
        new_entry = {
            "Names": [name],
            "A/C No:": [account_no],
            "Balance:": [init_balance],
            "Sign:": [sign],
            "Mobile_No:": [mobile_no],
            "Adhar_No:": [adhar_no],
            "Time:": [time],
            "AC_TYPE": [ac_type]
        }
        df = pd.DataFrame(new_entry)
        
        # Append to the file if it exists
        if os.path.isfile(accounts_file):
            with pd.ExcelWriter(accounts_file, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                df.to_excel(writer, index=False, header=False, startrow=writer.sheets['Sheet1'].max_row)
        else:
            with pd.ExcelWriter(accounts_file, engine='openpyxl', mode='w') as writer:
                df.to_excel(writer, index=False)

    @staticmethod
    def closed(name, account_no, sign, mobile_no, adhar_no, time, reason, closed_file):
        entry = {
            "Names": [name],
            "A/C No:": [account_no],
            "Sign:": [sign],
            "Mobile_No:": [mobile_no],
            "Adhar_No:": [adhar_no],
            "Time:": [time],
            "Reason": [reason]
        }
        df = pd.DataFrame(entry)
        
        # Append to the file if it exists
        if os.path.isfile(closed_file):
            with pd.ExcelWriter(closed_file, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                df.to_excel(writer, index=False, header=False, startrow=writer.sheets['Sheet1'].max_row)
        else:
            with pd.ExcelWriter(closed_file, engine='openpyxl', mode='w') as writer:
                df.to_excel(writer, index=False)

