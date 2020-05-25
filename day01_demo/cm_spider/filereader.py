import json
import os
from .db import dbconnect


def read(filePath):
    """
    读取文件内容
    :param filePath:
    :return:
    """
    data = ""
    with open(filePath, "r", encoding='UTF-8') as f:
        data = f.read()
    return data


def jsonToObject(jsonContent):
    return json.loads(jsonContent)


def dataAdd(filePath):
    """
    添加数据到数据库
    :param filePath:
    :return:
    """
    jsonContent = read(filePath)
    datas = jsonToObject(jsonContent)
    for item in datas:
        print(item["title"])
        postInfo, count = dbconnect.findOne(item["platformId"], item["platformPostToken"])
        if count == 0:
            dbconnect.addData(item)


def forFile(mkdirPath):
    """
    遍历文件夹
    :param mkdirPath:
    :return:
    """
    for root, dirs, files in os.walk(mkdirPath):
        for f in files:
            filePath = mkdirPath + "/" + f.title()
            if f.title().lower().find("txt") > 0:
                dataAdd(filePath)
