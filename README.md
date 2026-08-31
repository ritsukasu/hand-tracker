# Hand Tracking

This project uses OpenCV and MediaPipe to detect hands in a webcam feed and draw landmarks on the screen.

## Features

- Opens the default camera
- Detects one or two hands
- Draws hand landmarks and connections
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
