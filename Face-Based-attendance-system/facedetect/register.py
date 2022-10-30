
import cv2
import cv2                                                                      # openCV
import numpy as np                                                              # for numpy arrays
import mysql.connector
import argparse
from mysql.connector import Error
import os                                                                       # for creating folders





def insertOrUpdate(Id, Name,semester,section) :                                            # this function is for database
    connection = mysql.connector.connect(host='localhost',
                                         database='student',
                                         user='root',
                                         password='')
    connect = connection.cursor()
    # connecting to the database
                              # selecting the row of an id into consideration
    params = (Id,Name,semester,section)                                               # insering a new student data
    connect.execute("INSERT INTO studentdetails (id,name,semester,section)VALUES(%s,%s,%s,%s)", params)
    connection.commit()
    connect.close()
    connection.close()



Id = input('Enter user id : ')
name = input("Enter student's name : ")
semester = input("Enter semester: ")
section= input("Enter section : ")

insertOrUpdate(Id, name,semester,section)                                                  # calling the sqlite3 database

#C:\Users\Richard Lobo\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2\data\haarcascade_frontalface_default
face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # noise removal using iterative bilateral filters(removing noise and preserving edges

    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if faces is ():
        return None

    for (x, y, w, h) in faces:
        cropped_face = img[y:y + h, x:x + w]

    return cropped_face



cap = cv2.VideoCapture('C:/Users/Richard Lobo/Pictures/Camera Roll/WIN_20200210_10_19_20_Pro.mp4')
count = 0

while True:
    ret, frame = cap.read()
    if face_extractor(frame) is not None:
        count += 1
        face = cv2.resize(face_extractor(frame), (200, 200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        cv2.imwrite("C:/xampp1/htdocs/facedetect/dataset/User." + str(Id) +"." + str(count) + ".jpg", face)

        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Face Cropper', face)
    else:
        print("Face not Found")
        pass

    if cv2.waitKey(1) == 13 or count == 100:
        break

cap.release()
cv2.destroyAllWindows()

print('Colleting Samples Complete!!!')