# 获取人脸面部特征
import os
import face_recognition
import cv2


def getFaceDatas():
    """
    获取文件夹下的人脸面部特征
    :return:
    """
    face_database_dir = "face_databases"
    user_names = []  # 存放用户名称
    user_faces_encodings = []  # 存放用户面部特征向量
    files = os.listdir(face_database_dir)  # 遍历文件夹下的文件
    for fileName in files:
        userName, _ = os.path.splitext(fileName)
        if userName.find("Stor") >= 0:
            continue
        user_names.append(userName)

        filePath = os.path.join(face_database_dir, fileName)
        print(filePath)
        img_capture = cv2.imread(filePath)
        face_locations = face_recognition.face_locations(img_capture)  # 识别人脸位置
        faceEncodings = face_recognition.face_encodings(img_capture, face_locations)  # 获取人脸面部特征,如果图片中有多个人脸，则返回多个人脸特征
        user_faces_encodings.append(faceEncodings[0])
    return user_names, user_faces_encodings


def faceCompare(imgObject, faceDiscernUser, faceLocations, userNameDb, userFaceEcodsDb):
    """
    匹配人脸
    :param imgObject:画面对象
    :param faceDiscernUser:要识别的用户
    :param faceLocations:画面中人脸的位置
    :param userNameDb:库中用户姓名
    :param userFaceEcodsDb:库中用户人脸特征向量
    :return:
    """
    # 识别画面中的人脸特征
    face_encodings = face_recognition.face_encodings(imgObject, faceLocations)
    userCompareResult = []

    for face_encoding in face_encodings:
        # 匹配画面中的人脸特征与库中的人脸特征
        compareResults = face_recognition.compare_faces(userFaceEcodsDb, face_encoding)
        # 匹配画面中的人脸特征与库中的人脸特征的相似度，相似度越低匹配越高
        xiangsidu = face_recognition.face_distance(userFaceEcodsDb, face_encoding)
        print(xiangsidu)
        print(compareResults)
        name = "UnKnown"
        for index, is_match in enumerate(compareResults):
            if len(faceDiscernUser) > 0:
                if is_match and userNameDb[index] == faceDiscernUser and xiangsidu[index] < 0.3:
                    name = userNameDb[index]
                    break
            else:
                if is_match and xiangsidu[index] < 0.3:
                    name = userNameDb[index]
                    break
        userCompareResult.append(name)
    return userCompareResult
