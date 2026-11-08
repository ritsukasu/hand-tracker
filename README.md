# Hand Tracking

This project uses OpenCV and MediaPipe to detect hands in a webcam feed and draw landmarks on the screen.

## Features

- Opens the default camera
- Detects one or two hands
- Draws hand landmarks and connections<h1 align="center">Hand Tracking</h1>

<p align="center">
  Real-time hand detection from your webcam, built with OpenCV and MediaPipe.
</p>

<p align="center">
  <img alt="Python 3.9+" src="https://img.shields.io/badge/Python-3.9%2B-3776ab?logo=python&amp;logoColor=white">
  <img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-vision-5c3ee8?logo=opencv&amp;logoColor=white">
  <img alt="MediaPipe" src="https://img.shields.io/badge/MediaPipe-hands-0097a7">
  <img alt="Status: practice project" src="https://img.shields.io/badge/status-practice%20project-orange">
</p>

A small practice project that opens your webcam, finds up to two hands in the frame, and draws their landmarks and connections live. It also measures the gap between your thumb tip and index fingertip and shows it on the video in pixels.

## Features

- Opens the default camera, with a fallback if it is unavailable
- Detects one or two hands at a time
- Draws hand landmarks and the connections between them
- Measures the distance between the thumb tip and index fingertip
- Displays that distance in pixels on the video frame

## Requirements

- Python 3.9 or newer
- [OpenCV](https://opencv.org)
- [MediaPipe](https://developers.google.com/mediapipe)

## Quick start

```bash
pip install opencv-python mediapipe
python "hand tracking.py"
```

A window will open with your webcam feed. Hold a hand up to the camera and the landmarks will appear.

## Controls

| Key | Action |
| --- | ------ |
| Q   | Quit the application |

## Built with

- [OpenCV](https://opencv.org) for camera capture and drawing
- [MediaPipe](https://developers.google.com/mediapipe) for hand landmark detection

## License

No license has been added yet.
- Measures the distance between the thumb tip and index fingertip
- Displays the distance in pixels on the video frame

## Requirements

- Python 3.9+
- OpenCV
- MediaPipe

Install dependencies with:

```bash
pip install opencv-python mediapipe
```

## Run

```bash
python "hand tracking.py"
```

## Controls

- Press Q to quit the application.

## Notes

The script attempts to use the default webcam and will fall back if needed.
