import cv2
import numpy as np


def  empty(a):
    pass

path = "/Users/anubhav/Desktop/car.png"

cv2.namedWindow("TrackBars")

cv2.resizeWindow("TrackBars",640,340)



cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)

cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)

cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val MAx","TrackBars",255,255,empty)



while True:


    img= cv2.imread(path)

    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","Trackbar")
    h_max = cv2.getTrackbarPos("Hue Max","Trackbar")

    s_min = cv2.getTrackbarPos("Sat Min","Trackbar")
    s_max = cv2.getTrackbarPos("Sat Max","Trackbar")

    v_min = cv2.getTrackbarPos("Val Min","Trackbar")
    v_max = cv2.getTrackbarPos("Val Max","Trackbar")




    print(h_min,h_max,s_min, s_max ,v_min ,v_max)

    lower= np.array([h_min,s_min,v_min])
    upper= np.array([h_max,s_max,v_max])

    mask= cv2.inRange(imgHSV,lower,upper)


    cv2.imshow("Original",img)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask",mask)

    cv2.waitKey(1)

