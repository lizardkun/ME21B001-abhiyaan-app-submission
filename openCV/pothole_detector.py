import cv2
import numpy as np

cap = cv2.VideoCapture('/home/aahana/Downloads/pothole.mp4')
frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))

frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))



ret, frame1 = cap.read()
ret, frame2 = cap.read()
print(frame1.shape)
while cap.isOpened():
    gray = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    ret,gray = cv2.threshold(gray,127,255,0)
    gray2 = gray.copy()
    mask = np.zeros(gray.shape,np.uint8)
    contours, hier = cv2.findContours(gray,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if 100<cv2.contourArea(cnt)<700:
            (x, y, w, h) = cv2.boundingRect(cnt)
            cv2.drawContours(frame1,[cnt],0,(0,255,0),2)
            cv2.drawContours(mask,[cnt],0,255,-1)
            if cv2.contourArea(cnt) < 500:
                continue
            cv2.rectangle(mask, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("feed", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()
    if cv2.waitKey(40) == 27:
            break


cv2.waitKey(0)
cv2.destroyAllWindows()