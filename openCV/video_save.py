import cv2 as cv

vdo=cv.VideoCapture(0) 

fourcc=cv.VideoWriter_fourcc(*"H264")
save=cv.VideoWriter('saved_video.avi[]',fourcc,20.0,(680,640))

while(vdo.isOpened()):# isopened is check file is existing or not
    ret,frame=vdo.read()

    cv.imshow("video",frame)
    
    if ret==True:
        save.write(frame)
    
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
vdo.release()
save.release()
cv.destroyAllWindows()