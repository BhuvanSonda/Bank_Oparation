import cv2 as cv
import datetime as dt

vdo=cv.VideoCapture(0)

while (vdo.isOpened):
    ret, frame = vdo.read()

    time=dt.datetime.now()
    C_time=time.strftime( "%H:%M:%S")
    D_date=time.strftime("%d/%m/%Y")

    text1= f"date : {D_date}"
    text2=f"Time : {C_time}"

    cv.putText(frame, text1, (10, 30), cv.FONT_HERSHEY_TRIPLEX,1,(0,28,225),2)
    cv.putText(frame, text2, (10, 70), cv.FONT_HERSHEY_TRIPLEX,1,(30,30,225),2)

    cv.imshow("video",frame)

    if cv.waitKey(1) & 0xFF==ord("q"):
        break


vdo.release()
cv.destroyAllWindows()