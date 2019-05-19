#since many of us were getting an error  " error: OpenCV(4.1.0) C:\projects\opencv-python\opencv\modules\objdetect\src\cascadedetect.cpp:1658: error: (-215:Assertion failed) !empty() in function 'cv::CascadeClassifier::detectMultiScale' "
# to encounter the error in facecascade I made this

import cv2  

#importing file from directory 
img = cv2.imread("anipic.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

faces = faceCascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors = 5)

print(type(faces))
print(faces)

for(x,y,w,h) in faces:
    img = cv2.rectangle(img,(x, y),(x+w, y+h), (255, 0, 0), 3)
    cv2.imshow("sample",img)
    cv2.waitKey(0)
    resized = cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))
    cv2.imshow("Gray", resized)
    cv2.waitKey(0)
    
cv2.waitKey(0)
cv2.destroyAllWindows()
