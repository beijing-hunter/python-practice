import cv2
import face_recognition
import numpy as np

# 读取图片
img_capture = cv2.imread("imges/121612.jpg")

# 从图片中提取出人的脸部所在区域（如果画面中有多个人脸，则返回多个人脸位置）
face_locations = face_recognition.face_locations(img_capture)
print(face_locations)
# 循环遍历人的脸部所在区域，并画框
for top, right, bottom, left in face_locations:
    color = (0, 255, 0)
    lineWide = 5
    cv2.rectangle(img_capture, (left, top), (right, bottom), color, lineWide)

cv2.imwrite("imges/face01.jpg", img_capture)  # 保存图片
