import numpy as np
import cv2 as cv
# # read webcam using cv
# cap = cv.VideoCapture(1)
# if cap.isOpened():
#     ret, frame = cap.read()
# else:
#     ret = False
# while ret:
#     ret, frame = cap.read()
#     cv.imshow("webcam", frame)
#     if cv.waitKey(25) & 0xFF ==ord("q"):
#         break
# cap.release()
# cv.destroyAllWindows()

# read webcam using cv
cap = cv.VideoCapture(0)  # Try 1, 2, or -1 if 0 doesn't work


# change the cam into grayscale cam
while True:
    ret, frame = cap.read()
    bgrhls = cv.cvtColor(frame, cv.COLOR_BGR2HLS) 
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)\
    
    cv.imshow("webcam", gray_frame)
    cv.imshow("webcam 2", bgrhls)    
    if cv.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()