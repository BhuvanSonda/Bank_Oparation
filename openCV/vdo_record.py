import cv2 as cv
# r is a prefix that helps to remove the specification of "\"slash
v_file=r"C:\Users\Docketrun\Videos\XVR_ch5_main_20211129110000_20211129112048.asf"

vdo=cv.VideoCapture(v_file) #instead of zero we can give valid file name with extension
ls=[]
while True:# isopened is check file is existing or not
    ret,frame=vdo.read()
    cv.imshow("video",frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
    
vdo.release()
cv.destroyAllWindows()