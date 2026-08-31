import math
import cv2
import mediapipe as mp

CAMERA_INDEX = 0

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

LANDMARK_COLOR = (203, 192, 255)
CONNECTION_COLOR = (203, 192, 255)
LINE_COLOR = (0, 255, 0)

landmark_spec = mp_drawing.DrawingSpec(color=LANDMARK_COLOR, thickness=-1, circle_radius=4)
connection_spec = mp_drawing.DrawingSpec(color=CONNECTION_COLOR, thickness=2)


def main():
    cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)
    if not cap.isOpened():
        cap = cv2.VideoCapture(CAMERA_INDEX)

    if not cap.isOpened():
        print(f"Could not open camera at index {CAMERA_INDEX}.")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    window_name = "Hand Tracking"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 1280, 720)

    with mp_hands.Hands(
        model_complexity=0,
        max_num_hands=2,
        min_detection_confidence=0.6,
        min_tracking_confidence=0.6,
    ) as hands:

        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                continue

            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rgb_frame.flags.writeable = False

            results = hands.process(rgb_frame)

            frame.flags.writeable = True
            h, w, _ = frame.shape

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        landmark_spec,
                        connection_spec,
                    )

                    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

                    x1, y1 = int(thumb_tip.x * w), int(thumb_tip.y * h)
                    x2, y2 = int(index_tip.x * w), int(index_tip.y * h)

                    cv2.line(frame, (x1, y1), (x2, y2), LINE_COLOR, 2)

                    distance = math.hypot(x2 - x1, y2 - y1)
                    mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2

                    cv2.putText(
                        frame,
                        f"{int(distance)}px",
                        (mid_x + 10, mid_y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        LINE_COLOR,
                        2,
                    )

            try:
                _, _, win_w, win_h = cv2.getWindowImageRect(window_name)
                if win_w > 0 and win_h > 0:
                    frame = cv2.resize(frame, (win_w, win_h))
            except cv2.error:
                pass

            cv2.imshow(window_name, frame)

            if cv2.waitKey(5) & 0xFF in (ord('q'), 27):
                break

            if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()