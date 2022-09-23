import cv2 as cv
import numpy as np

tracking = cv.TrackerKCF_create()
#tracking = cv.TrackerCSRT_create()

video = cv.VideoCapture('street.mp4')

ok, frame = video.read()

bbox = cv.selectROI(frame) # região de interesse 

#print(bbox)

ok = tracking.init(frame, bbox)

while True:
    ok, frame = video.read()
    if not ok: 
        break
    ok,bbox = tracking.update(frame)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, 1)
    else:
        cv.putText(frame, 'Error', (100, 80), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 255, 0), 2)


    cv.imshow('Tracking', frame)
    if cv.waitKey(1) & 0XFF == 27:
        break
    
