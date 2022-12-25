import cv2
import imutils
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img=cv2.imread(r'C:\Users\nicol\OneDrive\Desktop\marina\an 3\inteligenta artificiala\sem\6\nrmat.png')
#img=cv2.resize(img,(800,600))
#cv2.imshow('Imagine redimensionata',img)
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray=cv2.bilateralFilter(gray ,13,15,15)
cv2.imshow('imagine cu filtru gri', gray)
edget=cv2.Canny(gray, 30, 200)
contur=cv2.findContours(edget.copy(),cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contur=imutils.grab_contours(contur)
contur=sorted(contur,key=cv2.contourArea, reverse=True)[:10]
screenCnt=None
for c in contur:
    peri=cv2.arcLength(c, True)
    approx=cv2.approxPolyDP(c, 0.018 * peri, True)
    if len(approx)==4:
        screenCnt=approx
        break  
if screenCnt is None:
    detected=0
    print("nu a fot detectat nici un contur")
else:
    detected=1
mask=np.zeros(gray.shape,np.uint8)
new_image=cv2.drawContours(mask,[screenCnt],0,255,-1,)
new_image=cv2.bitwise_and(img,img,mask=mask)
(x,y)=np.where(mask==255)
(topx,topy)=(np.min(x), np.min(y))
(bottonx,bottony)=(np.max(x), np.max(y))
CROP=gray[topx:bottonx+1, topy:bottony+1]
text_numar=pytesseract.image_to_string(CROP, config='--psm 10')
img=cv2.resize(img,(500,300))
CROP=cv2.resize(gray,(400,200))
cv2.inshow('decupat', CROP)
cv2.waitKey(0)
cv2.destroyAllWindows()