from lxml import etree


def htmlParseFacotry(htmlContent, platformId):
    """
    html内容解析工厂
    """
    if platformId == 24:
        return ppParse(htmlContent)
    return htmlContent


def ppParse(htmlContent):
    """
    澎湃网新闻内容解析
    """
    htmlOb = etree.HTML(htmlContent, etree.HTMLParser())
    newContentList = htmlOb.xpath('//div[@class="news_txt"]/text()')
    print(newContentList)
    return str(newContentList);
