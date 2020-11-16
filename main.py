import cv2
import time


cv2.namedWindow("preview")  # Setting the window name to preview
vc = cv2.VideoCapture(0)  # This is how we access the camera, 0 is used as it is the first camera.

if vc.isOpened():  # checking if the camera is on, and if so we try to get the first frame.
    rval, frame = vc.read()
else:
    rval = False

while rval:
    rval, frame = vc.read()  # getting new frame data.

    face_cascade = cv2.CascadeClassifier("C:/Users/pass512cs15/PycharmProjects/Camera/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50)
    )

    img = cv2.imread("Test Sign.jpg")
    for (x,y,w,h) in faces:
        img[100:400, 100:400,:] = frame[100:400, 100:400,:]
        #cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),3)

    cv2.imshow("preview", img)  # Starting the camera preview giving it the frame.
    key = cv2.waitKey(10)
    if key == 27:  # exit on ESC
        break


cv2.destroyWindow("preview")
vc.release()
