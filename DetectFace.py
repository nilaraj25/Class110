import cv2 
import numpy as mp 
video=cv2.VideoCapture(0)

while True:
    check, frame= video.read()
    cv2.imshow("nila", frame)
    key=cv2.waitKey(1)
    if key==32:
        print("hello")
        break 

video.release()
