import cv2 as cv
import numpy as np

def main():

    return

def capture_video(path):

    cap = cv.VideoCapture(path)

    if(not(cap.isOpenend())):
        return

    while True:
        isTrue, frame = cap.read()
        cv.imshow('Video', frame)

        if(cv.waitKey(20) & 0xFF == ord('d')):
           break

    cap.release()
    cv.destroyAllWindows()
    cv.waitKey(0)
