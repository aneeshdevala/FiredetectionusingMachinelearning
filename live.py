# This script will detect faces via your webcam.
# Tested with OpenCV3

import cv2

import matplotlib.pyplot as plt
cap = cv2.VideoCapture(0)

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("E:/haarcascade_frontalface_default.xml")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        #flags = cv2.CV_HAAR_SCALE_IMAGE
    )


    if len(faces)>0:
                print("Fire Detection Found Waiting for Send Intimation"
                      "".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):

        break
img_RGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
img_cap = plt.imshow(img_RGB)
plt.savefig("test.png")
plt.show()
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

