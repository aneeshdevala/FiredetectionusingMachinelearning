    import cv2
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import numpy as np

import matplotlib.pyplot as plt

live_Camera = cv2.VideoCapture(0)

lower_bound = np.array([11, 33, 111])

upper_bound = np.array([90, 255, 255])

while (live_Camera.isOpened()):

    ret, frame = live_Camera.read()

    frame = cv2.resize(frame, (1280, 720))

    frame = cv2.flip(frame, 1)

    frame_smooth = cv2.GaussianBlur(frame, (7, 7), 0)

    mask = np.zeros_like(frame)

    mask[0:720, 0:1280] = [255, 255, 255]

    img_roi = cv2.bitwise_and(frame_smooth, mask)

    frame_hsv = cv2.cvtColor(img_roi, cv2.COLOR_BGR2HSV)

    image_binary = cv2.inRange(frame_hsv, lower_bound, upper_bound)

    check_if_fire_detected = cv2.countNonZero(image_binary)

    if int(check_if_fire_detected) >= 20000:
        cv2.putText(frame, "Fire Detected !", (300, 60), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 2)

    cv2.imshow("Fire Detection", frame)
    msg = MIMEMultipart()
    msg['Subject'] = 'Fire Detection Image Mail123'
    msg['From'] = 'hasidata@gmail.com'
    msg['To'] = 'sjnair99@gmail.com'
    print("in func")
    text = MIMEText("Fire Detected from cam 1")
    msg.attach(text)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('hasidata@gmail.com', 'ranji@276')
    s.sendmail('sjnair99@gmail.com', 'sjnair99@gmail.com', msg.as_string())

    s.quit()

    print("Sent Successfully")

    if cv2.waitKey(10) == 27:
        break

live_Camera.release()

cv2.destroyAllWindows()
