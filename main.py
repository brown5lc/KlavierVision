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
        # roi = frame[roiY_start:roiY_end, roiX_start:roiX_end]
        # blur = cv.GaussianBlur(frame, (5, 5), 0)
        grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        _, thresh = cv.threshold(grey, 127, 255, cv.THRESH_BINARY)
        edges = cv.Canny(thresh, 50, 150)
        contours, _ = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        cv.drawContours(frame, contours, -1, (255, 0, 0), 2)
        # cv.imshow('Contours', frame)

        key_contours = []
        for contour in contours:
            if 1000 < cv.contourArea(contour) < 5000:
                approx = cv.approxPolyDP(contour, 0.02 * cv.arcLength(contour, True), True)
                if len(approx) == 4:
                    key_contours.append(contour)

        cv.drawContours(frame, key_contours, -1, (0, 0, 255), 2)

        key_regions = [
            (100, 200, 150, 400),
        ]

        for region in key_regions:
            x_start, y_start, x_end, y_end = region
            cv.rectangle(frame, (x_start, y_start), (x_end, y_end),  (0, 255, 0), 2)
            cv.putText(frame, 'Key', (x_start, y_start - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        cv.imshow('Keys', frame)

        if(cv.waitKey(20) & 0xFF == ord('d')):
           break

    cap.release()
    cv.destroyAllWindows()
    cv.waitKey(0)

capture_video('videos/piano2.mp4')
