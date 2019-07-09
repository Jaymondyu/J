
import sys

import cv2

import face_recognition # 人脸识别库  dlib


# 读取图片
face_image = face_recognition.load_image_file(r'./face/face.jpg')

# 特征提取
face_encodings = face_recognition.face_encodings(face_image)

# print(face_encodings)
face_locations = face_recognition.face_locations(face_image) # 特征的位置提取

# 判断图片中出现的人数

n = len(face_encodings)
if n>2:
    print("超过两个人") # 人数多于两个
    sys.exit() # 程序自动结束

try:
    face1 = face_encodings[0]
    face2 = face_encodings[1]
except:
    print('error')
    sys.exit()


# 特征对比
result = face_recognition.compare_faces([face1],face2,tolerance=0.6)

if result == [True]:
    name = "PASS"
else:
    name = "DENIED"


# 绘图

for i in range(len(face_encodings)):
    face_encoding = face_encodings[(i-1)]
    face_location = face_recognition.face_locations([i-1])

    # 画框
    top, right,bottom,left = face_location

    cv2.rectangle(face_image,(left,top),(right,bottom),(0,255,0),2)

    # 写内容
    cv2.putText(face_image,name,(left-10,top-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2)

face_image_rgb = cv2.cvtColor(face_image,cv2.COLOR_BGR2RGB)

# 展示图像
cv2.imshow('output',face_image_rgb)

cv2.waitKey(0)