# Hand Tracking

> Your webcam, a pair of hands, and a little bit of geometry.

[Overview](#overview) | [Setup](#setup) | [How it works](#how-it-works) | [Controls](#controls) | [Tech](#tech)

---

## Overview

Hand Tracking is a small practice project that uses OpenCV and MediaPipe to find hands in a live webcam feed. It draws each hand's landmarks on screen and measures how far apart your thumb tip and index fingertip are, in pixels.

| | |
| --- | --- |
| **Language** | Python 3.9+ |
| **Libraries** | OpenCV, MediaPipe |
| **Input** | Default webcam, with a fallback if needed |
| **Hands detected** | One or two |
| **Output** | Live video with landmarks, connections, and a pixel distance readout |

## Setup

Install the dependencies:

```bash
pip install opencv-python mediapipe
```

Run the script:

```bash
python "hand tracking.py"
```

A window opens with your camera feed. Hold a hand in front of the lens and the landmarks appear.

## How it works

1. The script opens the default camera and reads frames continuously.
2. Each frame is passed to MediaPipe, which looks for up to two hands.
3. Detected landmarks and the connections between them are drawn onto the frame.
4. The thumb tip and index fingertip positions are compared to get the distance between them.
5. That distance is printed on the video in pixels.

## Controls

Press `Q` to quit.

## Tech

- [OpenCV](https://opencv.org) handles camera capture and drawing.
- [MediaPipe](https://developers.google.com/mediapipe) handles hand landmark detection.

## License

No license has been added yet.
