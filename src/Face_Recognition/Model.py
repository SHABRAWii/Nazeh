import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import Data_Management.AttendanceManager as AttendanceManager
import UI.UI as UI
# from PIL import ImageGrab

path = 'src/Database'
images = []
classNames = []
myList = os.listdir(path)
# print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
# print(classNames)


def findEncodings(images):

    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString},Done')

# FOR CAPTURING SCREEN RATHER THAN WEBCAM
# def captureScreen(bbox=(300,300,690+300,530+300)):
#     capScr = np.array(ImageGrab.grab(bbox))
#     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
#     return capScr

encodeListKnown = findEncodings(images)
# print('Encoding Complete')
def start(camID, showUI = True, factor = 0.25, fast = 0):
    print("CamID: " + str(camID) + " ShowCase: " + str(showUI) + " Factor: " + str(factor) + " Model: " + str(fast))
    cap = cv2.VideoCapture(camID)
    factor = float(factor)
    locations_model = 'cnn'
    encoding_model = 'large'
    if fast:
        locations_model = 'hog'
        if fast > 1:
            encoding_model = 'small'
    while True:
        success, img = cap.read()
        # img = captureScreen()
        imgS = cv2.resize(img, (0, 0), None, fx = factor, fy = factor)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS, 1, locations_model)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame, 1, encoding_model)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                UI.Update_computerVision(name)

                # print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1+6, y2-6),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
                AttendanceManager.addAttendance(name, 1, 0)
                # markAttendance(name)
        if showUI:
            cv2.imshow('Webcam', img)
        cv2.waitKey(1)
