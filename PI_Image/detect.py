
# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
from LED import *
import numpy as np
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 640)
camera.framerate = 60
rawCapture = PiRGBArray(camera, size=(640, 640))

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    try:
        image = frame.array
        # Change to gray
        im = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        params = cv2.SimpleBlobDetector_Params()
        # Filter by thresholds
        params.filterByColor = 1
        params.minThreshold = 0
        params.maxThreshold = 100
        # Filter by area.
        params.filterByArea = 1
        params.minArea = 600
        params.maxArea = 48000
        # Filter by shape
        # Circularity
        params.filterByCircularity = 1
        params.minCircularity = 0.1
        # params.maxCircularity = 1
        # Convexity
        params.filterByConvexity = 1
        params.minConvexity = 0.1
        # params.maxConvexity = 1
        # Inertia
        params.filterByInertia = 1
        params.minInertiaRatio = 0.01
        # params.maxInertiaRatio =  1
        # Create a detector with the parameters
        ver = (cv2.__version__).split('.')
        if int(ver[0]) < 3 :
            detector = cv2.SimpleBlobDetector(params)
        else :
            detector = cv2.SimpleBlobDetector_create(params)
        keypoints = detector.detect(im)
        if len(keypoints) >= 1 or cv2.minMaxLoc(im)[0]==0:
                light()
        else:
                shutdown()
        #im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        #cv2.imshow("KeyPoints", im_with_keypoints)
        #cv2.waitKey(0)
        rawCapture.truncate(0)
    except KeyboardInterrupt:
        break
