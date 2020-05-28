import cv2
import face_recognition
import numpy as np
from face_tezheng_03 import *

# 读取图片
img_capture = cv2.imread("imges/Z0469.jpg")
userNames, userfaceEcods = getFaceDatas()

# 从图片中提取出人的脸部所在区域（如果画面中有多个人脸，则返回多个人脸位置）
face_locations = face_recognition.face_locations(img_capture)
userCompareResults = faceCompare(img_capture, '', face_locations, userNames, userfaceEcods)
print(face_locations)
# 循环遍历人的脸部所在区域，并画框
for (top, right, bottom, left), name in zip(face_locations, userCompareResults):
    color = (0, 255, 0)
    lineWide = 5
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.rectangle(img_capture, (left, top), (right, bottom), color, lineWide)
    print(name)
    cv2.putText(img_capture, name, (left, top - 10), font, 3, 1)

cv2.imwrite("imges/face01.jpg", img_capture)  # 保存图片
