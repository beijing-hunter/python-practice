import requests
from .db import dbconnect


def getHtmlContent(hrefUrl,platformId):
    htmlContent = ""
    try:
        headers = {
            'Accept-Encoding':'',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }
        response = requests.get(hrefUrl,headers=headers,timeout=2)
        if platformId==8:
            htmlContent = response.content.decode("ISO-8859-1")
        else:
            htmlContent = response.content.decode()

    except Exception as e:
        print(e)
    finally:
        return htmlContent


def filterKey(hrefUrl,platformId):
    filterKey = ["两会", "提案", "医疗", "医生", "医保", "新闻发布会", "公共卫生", "临床", "应急管理体系", "防控", "医院", "医学", "药", "卫生事业", "诊断",
                 "医护人员", "医务人员", "病", "职称", "论文", "规培", "诊疗", "补助", "医闹", "伤医", "医患关系", "健康", "疾病预防", "健康中国", "中医",
                 "中西医", "处方", "疫苗", "筛查", "疾病", "器械", "生物制品", "医养结合", "基层医疗", "基层医生"]

    htmlContent = getHtmlContent(hrefUrl,platformId)
    inKey = []
    for key in filterKey:
        if htmlContent.find(key) >= 0:
            inKey.append(key)
    return inKey


def filterData():
    postDatas = dbconnect.findAll()
    for postInfo in postDatas:
        print(postInfo["linkUrl"])
        inKeys = filterKey(postInfo["linkUrl"],postInfo["platformId"])
        if len(inKeys) > 0:
            postInfo["status"] = 2
            postInfo["inKeys"] = ','.join(inKeys)
            dbconnect.updateInfo(postInfo)
