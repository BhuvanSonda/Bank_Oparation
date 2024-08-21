import cv2 as cv

cap= cv.VideoCapture(r"C:\Users\Docketrun\Videos\XVR_ch5_main_20211129110000_20211129112048.asf")

mog=cv.createBackgroundSubtractorMOG2()

while True:
    ret,frame=cap.read()
    if not ret:
        break
    fgmask=mog.apply(frame)
    cv.imshow('Original',frame)
    cv.imshow('MOG2',fgmask)
    canny=cv.Canny(frame,50,150)
    cv.imshow('Canny edge',canny)

    if cv.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv.destroyAllWindows()