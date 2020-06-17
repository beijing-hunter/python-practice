import cv2
import face_recognition
from face_tezheng_03 import *

# 打开摄像头，获取摄像头对象
video_capture = cv2.VideoCapture(0)  # 0代表的是第一个摄像头
userNames, userfaceEcods = getFaceDatas()  # 获取库中存放的人脸数据
faceDiscernUser = ""  # 识别指定人的

# 循环不停的去获取摄像头拍摄到的画面，并做进一步的处理
while True:
    ret, frame = video_capture.read()  # frame 摄像头所拍摄的画面
    # 从拍摄的画面中提取出人的脸部所在区域（如果画面中有多个人脸，则返回多个人脸位置）
    face_locations = face_recognition.face_locations(frame)
    # 识别画面中的人脸
    userCompareResults = faceCompare(frame, faceDiscernUser, face_locations, userNames, userfaceEcods)

    # 循环遍历人的脸部所在区域，并画框
    for (top, right, bottom, left), name in zip(face_locations, userCompareResults):
        color = (0, 255, 0)
        lineWide = 1
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.rectangle(frame, (left, top), (right, bottom), color, lineWide)
        print(name)
        cv2.putText(frame, name, (left, top - 10), font, 0.5, 1)

    cv2.imshow("Video", frame)  # 通过opencv把拍摄到的画面展示出来
    # 设定按q退出while，退出程序的这样一个机制
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
