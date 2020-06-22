from lxml import etree


def htmlParseFacotry(htmlContent, platformId):
    """
    html内容解析工厂
    """
    if platformId == 24:
        return ppParse(htmlContent)
    if platformId == 16:
        return xinJingBao(htmlContent)
    return htmlContent


def ppParse(htmlContent):
    """
    澎湃网新闻内容解析
    """
    htmlOb = etree.HTML(htmlContent, etree.HTMLParser())
    newContentList = htmlOb.xpath('//div[@class="news_txt"]/text()')
    return str(newContentList);


def xinJingBao(htmlContent):
    """
    新京报内容解析
    """
    htmlOb = etree.HTML(htmlContent, etree.HTMLParser())
    newContentList = htmlOb.xpath('//div/p/text()')
    return str(newContentList)
