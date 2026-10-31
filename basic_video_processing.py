"""Basic Video Processing methods."""
import os
import cv2


ID1 = '123456789'
ID2 = '987654321'

INPUT_VIDEO = 'atrium.avi'
GRAYSCALE_VIDEO = f'{ID1}_{ID2}_atrium_grayscale.avi'
BLACK_AND_WHITE_VIDEO = f'{ID1}_{ID2}_atrium_black_and_white.avi'
SOBEL_VIDEO = f'{ID1}_{ID2}_atrium_sobel.avi'


def get_video_parameters(capture):
    """Get an OpenCV capture object and extract its parameters.
    Args:
        capture: VideoCapture object. The input video's VideoCapture.
    Returns:
        parameters: dict. A dictionary of parameters names to their values.
    """
    fourcc = int(capture.get(cv2.CAP_PROP_FOURCC))
    fps = int(capture.get(cv2.CAP_PROP_FPS))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    parameters = {"fourcc": fourcc, "fps": fps, "height": height, "width": width}
    return parameters


def convert_video_to_grayscale(input_video_path, output_video_path):
    """Convert the video in the input path to grayscale.

    Use VideoCapture from OpenCV to open the video and read its
    parameters using the capture's get method.
    Open an output video using OpenCV's VideoWriter.
    Iterate over the frames. For each frame, convert it to gray scale,
    and save the frame to the new video.
    Make sure to close all relevant captures and to destroy all windows.

    Args:
        input_video_path: str. Path to input video.
        output_video_path: str. Path to output video.

    Additional References:
    (1) What are fourcc parameters:
    https://docs.microsoft.com/en-us/windows/win32/medfound/video-fourccs

    """
    """Exercise Solution Start"""
    cap = cv2.VideoCapture(input_video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    writer = cv2.VideoWriter(
        output_video_path,
        cv2.VideoWriter_fourcc(*"XVID"),
        fps,
        (width, height),
        isColor=False,  # For grayscale/binary frames.
    )

    while True:
        success, frame_in = cap.read()
        if not success:
            break  # last frame has been read, exit

        frame_out = cv2.cvtColor(frame_in, cv2.COLOR_BGR2GRAY)
        writer.write(frame_out)

    cap.release()
    writer.release()
    """End"""


def convert_video_to_black_and_white(input_video_path, output_video_path):
    """Convert the video in the input path to black and white.

    Use VideoCapture from OpenCV to open the video and read its
    parameters using the capture's get method.
    Open an output video using OpenCV's VideoWriter.
    Iterate over the frames. For each frame, first convert it to gray scale,
    then use OpenCV's THRESH_OTSU to slice the gray color values to
    black (0) and white (1) and finally convert the frame format back to RGB.
    Save the frame to the new video.
    Make sure to close all relevant captures and to destroy all windows.

    Args:
        input_video_path: str. Path to input video.
        output_video_path: str. Path to output video.

    Additional References:
    (1) What are fourcc parameters:
    https://docs.microsoft.com/en-us/windows/win32/medfound/video-fourccs

    """
    """Exercise Solution Start"""
    cap = cv2.VideoCapture(input_video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    writer = cv2.VideoWriter(
        output_video_path,
        cv2.VideoWriter_fourcc(*"XVID"),
        fps,
        (width, height),
        isColor=False,  # For grayscale/binary frames.
    )

    while True:
        success, frame_in = cap.read()
        if not success:
            break  # last frame has been read, exit

        frame_out = cv2.cvtColor(frame_in, cv2.COLOR_BGR2GRAY)  # color --> grayscale
        _, frame_out = cv2.threshold(frame_out, 0, 255, cv2.THRESH_OTSU)  #  grayscale --> B&W
        writer.write(frame_out)

    cap.release()
    writer.release()
    """Exercise Solution End"""



def convert_video_to_sobel(input_video_path, output_video_path):
    """Convert the video in the input path to sobel map.

    Use VideoCapture from OpenCV to open the video and read its
    parameters using the capture's get method.
    Open an output video using OpenCV's VideoWriter.
    Iterate over the frames. For each frame, first convert it to gray scale,
    then use OpenCV's THRESH_OTSU to slice the gray color values to
    black (0) and white (1) and finally convert the frame format back to RGB.
    Save the frame to the new video.
    Make sure to close all relevant captures and to destroy all windows.

    Args:
        input_video_path: str. Path to input video.
        output_video_path: str. Path to output video.

    Additional References:
    (1) What are fourcc parameters:
    https://docs.microsoft.com/en-us/windows/win32/medfound/video-fourccs

    """
    """Exercise Solution Start"""
    cap = cv2.VideoCapture(input_video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    writer = cv2.VideoWriter(
        output_video_path,
        cv2.VideoWriter_fourcc(*"XVID"),
        fps,
        (width, height),
        isColor=False,  # For grayscale/binary frames.
    )

    while True:
        success, frame_in = cap.read()
        if not success:
            break  # last frame has been read, exit

        frame_out = cv2.cvtColor(frame_in, cv2.COLOR_BGR2GRAY)  # color --> grayscale
        frame_out = cv2.Sobel(frame_out, ddepth=-1, dx=1, dy=1, ksize=5)  #  grayscale --> B&W
        writer.write(frame_out)

    cap.release()
    writer.release()
    """Exercise Solution End"""


def main():
    convert_video_to_grayscale(INPUT_VIDEO, GRAYSCALE_VIDEO)
    convert_video_to_black_and_white(INPUT_VIDEO, BLACK_AND_WHITE_VIDEO)
    convert_video_to_sobel(INPUT_VIDEO, SOBEL_VIDEO)


if __name__ == "__main__":
    main()
