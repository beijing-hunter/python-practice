import requests
from .db import dbconnect


def getHtmlContent(hrefUrl):
    response = requests.get(hrefUrl)
    return response.content.decode()


def filterKey(hrefUrl):
    filterKey = ["两会", "提案", "医疗", "医生", "医保", "新闻发布会", "公共卫生", "临床", "应急管理体系", "防控", "医院", "医学", "药", "卫生事业", "诊断",
                 "医护人员", "医务人员", "病", "职称", "论文", "规培", "诊疗", "补助", "医闹", "伤医", "医患关系", "健康", "疾病预防", "健康中国", "中医",
                 "中西医", "处方", "疫苗", "筛查", "疾病", "器械", "生物制品", "医养结合", "基层医疗", "基层医生"]

    htmlContent = getHtmlContent(hrefUrl)
    inKey = []
    for key in filterKey:
        if htmlContent.find(key) >= 0:
            inKey.append(key)
    return inKey


def filterData():
    postDatas = dbconnect.findAll()
    for postInfo in postDatas:
        print(postInfo["linkUrl"])
        inKeys = filterKey(postInfo["linkUrl"])
        if len(inKeys) > 0:
            postInfo["status"] = 2
            postInfo["inKeys"] = ','.join(inKeys)
            dbconnect.updateInfo(postInfo)
