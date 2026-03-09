import cv2
from utils import calculate_fps

cap = cv2.VideoCapture(0)

prev_time = 0

while True:
    success, frame = cap.read()

    if not success:
        print("Failed to grab frame")
        break

    fps, prev_time = calculate_fps(prev_time)

    # Put FPS on screen
    cv2.putText(frame, f"FPS: {int(fps)}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Webcam", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()