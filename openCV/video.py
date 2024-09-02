import cv2 as cv

vdo = cv.VideoCapture(0)

width = int(vdo.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(vdo.get(cv.CAP_PROP_FRAME_HEIGHT))

print(f'{width}x{height}')

fourcc = cv.VideoWriter_fourcc(*'DIVX')
record = cv.VideoWriter("v_save.avi", fourcc, 20.0, (width, height))

while vdo.isOpened():
    ret, frame = vdo.read()
    if not ret:
        print("End of video or cannot read frame.")
        break
    
    record.write(frame)

    cv.imshow("Video Frame", frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

vdo.release()
record.release()
cv.destroyAllWindows()
