import cv2
import numpy as np

cap = cv2.VideoCapture('masked.avi')

frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))

frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))



ret, frame1 = cap.read()
ret, frame2 = cap.read()
print(frame1.shape)
while cap.isOpened():
    #finding contours
    diff = cv2.absdiff(frame1, frame2)
    #finding contours in grayscale is easier
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    #gaussian blurring helps reduce noise
    blur = cv2.GaussianBlur(gray, (5,5), 100)
    _, thresh = cv2.threshold(blur, 30, 40, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        #i tried reducing the size of w and h so the bigger contour differences wouldnt get detected, like the trees and the roadlines, but reducimg the size not only includes them but also gives bonus white noise
        #detecting blobs didnt work either,"Segmentation fault (core dumped" is an error i frequently kept getting for the blob detection libraries i used
        if cv2.contourArea(contour) < 50 and w<50 and h<50:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    
    
    cv2.imshow("feed", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
out.release()