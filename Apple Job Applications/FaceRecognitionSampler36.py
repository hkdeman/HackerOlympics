import cv2
import numpy as np
import os
from PIL import Image

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)


name = input('Enter user name')
newpath = r'dataSet\\'+name 
if not os.path.exists(newpath):
    os.makedirs(newpath)
sampleNum=0
while(True):
    ret,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        sampleNum = sampleNum+1 
        cv2.imwrite(newpath+'\\'+str(sampleNum)+'.jpg',gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+y,y+h),(0,0,255),2)
        cv2.waitKey(100)
    cv2.imshow("Face",img)
    cv2.waitKey(1)
    if(sampleNum>80):
        break
cam.release()
cv2.destroyAllWindows()

recognizer = cv2.face.LBPHFaceRecognizer_create();

path = ('dataSet\\'+name,1)

def getImagesWithID(path):
    imagePaths=[]
    faces=[]
    IDs=[]
   
    imagePaths=[os.path.join(path[0],f) for f in os.listdir(path[0])]
    
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg,'uint8')
##        ID = int(os.path.split(imagePath[0])[-1].split('.')[0])
        faces.append(faceNp)
        IDs.append(path[1])
        cv2.imshow("training...",faceNp)
        cv2.waitKey(10)
    return IDs, faces


IDs, faces = getImagesWithID(path)
recognizer.train(faces,np.array(IDs))
recognizer.write('recognizer/trainingData.yml')

cv2.destroyAllWindows()


faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read('recognizer\\trainingData.yml')
user_id=0
##font = cv2.initFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
while(True):
    ret,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        user_id,conf = rec.predict(gray[y:y+h,x:x+w])
        if(user_id==1):
            user_id=name
        else:
            user_id="Unknown"
        cv2.putText(img,str(user_id),(x,y+h),cv2.FONT_HERSHEY_SIMPLEX,2,cv2.LINE_AA)
    cv2.imshow("Face",img)
    if(cv2.waitKey(1)==ord('q')):
        break

cam.release()
cv2.destroyAllWindows()

    
