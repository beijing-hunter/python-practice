from cm_spider import filereader,contentfilter,htmlparse

filereader.forFile("/Users/cmt/Desktop/cmt/zixun/")
contentfilter.filterData()
#content=contentfilter.getHtmlContent("https://www.thepaper.cn/newsDetail_forward_7885361",23)
#print(content)
#parseValue=htmlparse.ppParse(content)
#print("data type=%s,data value=%s" % (type(parseValue), parseValue))