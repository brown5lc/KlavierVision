import cv2 as cv
import numpy as np

def capture_video(path):
    roiX_start = 50
    roiY_start = 150
    roiX_end = 800
    roiY_end = 400

    cap = cv.VideoCapture(path)

    if(not(cap.isOpened())):
        return

    while True:
        isTrue, frame = cap.read()
        roi = frame[roiY_start:roiY_end, roiX_start:roiX_end]
        # blur = cv.GaussianBlur(frame, (5, 5), 0)
        grey = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
        _, thresh = cv.threshold(grey, 127, 255, cv.THRESH_BINARY)
        edges = cv.Canny(thresh, 50, 150)
        cv.imshow('Video', edges)

        contours, _ = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        cv.drawContours(frame, contours, -1, (0, 255, 0), 2)
        cv.imshow('Contours', frame)

        if(cv.waitKey(20) & 0xFF == ord('d')):
           break

    cap.release()
    cv.destroyAllWindows()
    cv.waitKey(0)

capture_video('videos/piano.mp4')
