import cv2
import keyboard
cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier(r'C:\Users\nicol\OneDrive\Desktop\marina\an 3\inteligenta artificiala\sem\8\text.xml')
while not keyboard.is_pressed('esc'):
    _,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,4)
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w, y+h),(255,0,0),2)
    cv2.imshow('img: ', img)
    k=cv2.waitKey(30) & 0xff
    if k==27:
       break
cap.release()