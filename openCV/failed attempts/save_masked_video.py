import cv2
import numpy as np

cap1 = cv2.VideoCapture("pothole.mp4")

while(1):

    _, frame = cap1.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of white color in HSV
    # change it according to your need !
    lower_white = np.array([0,0,0], dtype=np.uint8)
    upper_white = np.array([0,0,255], dtype=np.uint8)

    # Threshold the HSV image to get only white colors
    mask = cv2.inRange(hsv, lower_white, upper_white)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('res', res)
    cv2.imshow('mask', mask)
    video = cv2.VideoCapture('res')
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))
    
    size = (frame_width, frame_height)
    result = cv2.VideoWriter('masked.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)
    while(True):
        ret, frame = video.read()
    
        if ret == True: 
    
            # Write the frame into the
            # file 'filename.avi'
            result.write(frame)
    
            # Display the frame
            # saved in the file
            cv2.imshow('Frame', frame)
    
            # Press S on keyboard 
            # to stop the process
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
    
        # Break the loop
        else:
            break
    video.release()
    result.release()
    
        


   
    k = cv2.waitKey(5) & 0xFF
    if cv2.waitKey(40) == 27:
        break
        
