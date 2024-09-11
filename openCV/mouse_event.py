import cv2 as  cv
import numpy as np

# def draw(event,x,y,flag,params):
#     if event == cv.EVENT_LBUTTONDOWN:
#         # cv.putText(img,'cat', (x, y), cv.FONT_HERSHEY_TRIPLEX,0.5, (0, 0, 255), 2, cv.LINE_8)
#         #cv.circle(img,(x,y),100,(1,1,0))
#         int(x)
#         int(y)
#         poly = np.array([[x+20,y+40],[x+20,y+50],[x+80,y+90],[x+10,y+30]], np.int32)
#         cv.polylines(img, [poly], isClosed=True, color=(0, 255, 0), thickness=3)

# img=cv.imread('openCV/cat.jpg',1)
# cv.namedWindow('image')
# cv.setMouseCallback('image',draw)
# while True:
#     cv.imshow('image',img)
#     if cv.waitKey(1) & 0xFF== ord('q'):
#         break
# cv.destroyAllWindows()






# Global variables to keep track of the dragging state
dragging = False
start_x, start_y = -1, -1
rectangles = []
co_ord={"start_pt":[],'end_pt':[]}

# Mouse callback function
def mouse_callback(event, x, y, flags, param):
    global dragging, start_x, start_y, rectangles
    
    if event == cv.EVENT_LBUTTONDOWN:
        # On left button down, record the start position
        start_x, start_y = x, y
        co_ord["start_pt"].append(f'({x},{y})')
        cv.circle(img,(start_x,start_y),4,(0,0,255),-1)
        dragging = True
        
            
    elif event == cv.EVENT_LBUTTONUP:
        # On left button up, finalize the rectangle and stop dragging
        dragging = False
        co_ord["end_pt"].append(f'({x},{y})')
        rectangles.append(((start_x, start_y), (x, y)))
        cv.rectangle(img, (start_x, start_y), (x, y), (0, 255, 0), 2)
        cv.circle(img,(x,y),4,(0,0,255),-1)
        # cv.line(img,(start_x,start_y),(x,y),(0,0,255),2)
        cv.imshow('Drag and Drop', img)

# Create a image
img = cv.imread('openCV/cat.jpg', 1)#np.zeros((512, 512, 3), dtype=np.uint8)

# Create a window and set the mouse callback function
cv.namedWindow('Drag and Drop')
cv.setMouseCallback('Drag and Drop', mouse_callback,co_ord)

# Main loop to display the image
while True:
    cv.imshow('Drag and Drop', img)
    """Escape key to exit"""
    key = cv.waitKey(1)
    if key == 27: 
        
        break








# # Function to handle mouse events
# def draw(event, x, y, flags, param):
#     if event == cv.EVENT_LBUTTONDOWN:
#         co_ords_list = param  # Retrieve the list from params
#         co_ords_list.append((x, y))  # Append the new coordinates
#         cv.circle(img, (x, y), 5, (0, 0, 255),)  # Draw a circle at the clicked position

# img = cv.imread('openCV/cat.jpg', 1)


# cv.namedWindow('image')
# cv.setMouseCallback('image', draw, co_ord)  # Pass 'coords' as the params argument

# while True:
#     cv.imshow('image', img)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# print("Clicked coordinates:", co_ords)  # Print all stored coordinates after exiting



cv.destroyAllWindows()
print("starting point = ",co_ord['start_pt'])
print("starting point = ",co_ord['end_pt'])
