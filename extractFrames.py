import cv2 as cv
import os

def extract_frames(video_path, output_dir):
    cap = cv.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    frame_index = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_path = os.path.join(output_dir, f"frame_{frame_index:04d}.jpg")
        cv.imwrite(frame_path, frame)
        frame_index += 1

    cap.release()
    print(f"Extracted {frame_index} frames to {output_dir}")

extract_frames('videos/piano2.mp4', 'frames')