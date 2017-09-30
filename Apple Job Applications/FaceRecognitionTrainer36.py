import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create();
paths = [('dataSet\\Hemang',1),('dataSet\\Leo',2)]
def getImagesWithID(paths):
    imagePaths=[]
    for path in paths:
        imagePaths.append(([os.path.join(path[0],f) for f in os.listdir(path[0])],path[1]))
    faces=[]
    IDs=[]
    
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath[0]).convert('L')
        faceNp = np.array(faceImg,'uint8')
##        ID = int(os.path.split(imagePath[0])[-1].split('.')[0])
        faces.append(faceNp)
        IDs.append(imagePath[1])
        cv2.imshow("training...",faceNp)
        cv2.waitKey(10)
    return IDs, faces

IDs, faces = getImagesWithID(paths)
recognizer.train(faces,np.array(IDs))
recognizer.write('recognizer/trainingData.yml')

cv2.destroyAllWindows()
