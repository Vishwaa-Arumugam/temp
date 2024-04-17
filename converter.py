import cv2
import os


def extract_frames(video_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    fps = video_capture.get(cv2.CAP_PROP_FPS)

    # Initialize variables
    frame_count = 0
    success, frame = video_capture.read()

    while success:
        # Extract frame every second
        if frame_count % int(fps) == 0:
            frame_filename = os.path.join(output_folder, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_filename, frame)

        success, frame = video_capture.read()
        frame_count += 1

    # Release the VideoCapture object
    video_capture.release()


# Example usage:
video_path = "E:\code\premalu_project\premalu.mkv"
output_folder = "extracted_frames"
extract_frames(video_path, output_folder)
