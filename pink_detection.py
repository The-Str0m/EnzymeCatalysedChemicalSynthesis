import cv2
import numpy as np


cam_url = "http://172.20.10.12:81/stream"

#minimum threshold for pink
threshold = 40.0

#pink thresholds
lower_pink = np.array([140, 50, 50])
upper_pink = np.array([170, 255, 255])

#capture stream
cap = cv2.VideoCapture(cam_url)

if not cap.isOpened():
    print("couldn't connect to video stream")
    exit()

print("stream processing")

while True:
    ret, frame = cap.read()
    if not ret:
        print("couldn't fetch frames from camera")
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #mask
    pink_mask = cv2.inRange(hsv_frame, lower_pink, upper_pink)

    #calculate percentage
    total_pixels = frame.shape[0] * frame.shape[1]
    pink_pixels = cv2.countNonZero(pink_mask)
    pink_percentage = (pink_pixels / total_pixels) * 100


    if pink_percentage >= threshold:
        alert_text = f"pink detected ({pink_percentage:.1f}%)"
        text_color = (0, 0, 255)
    else:
        alert_text = f"searching for pink {pink_percentage:.1f}%"
        text_color = (0, 255, 0)

    cv2.putText(frame, alert_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 
                1, text_color, 2, cv2.LINE_AA)


    cv2.imshow("live stream processing", frame)
    cv2.imshow("pink mask", pink_mask)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
