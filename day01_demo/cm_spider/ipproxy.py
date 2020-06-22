from bs4 import BeautifulSoup
import requests
import random
from urllib import request, error


def getProxy(url):
    # 代理ip容器
    proxyIpDatas = []
    # 设置UA标识
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit '
                      '/ 537.36(KHTML, likeGecko) Chrome / 63.0.3239.132Safari / 537.36'
    }
    # page是我们需要获取多少页的ip，这里我们获取到第９页
    for page in range(1, 6):

        # 通过观察ＵＲＬ，我们发现原网址+页码就是我们需要的网址了，这里的page需要转换成str类型
        urls = "http://www.66ip.cn/areaindex_" + str(page) + "/1.html"
        # 通过requests来获取网页源码
        rsp = requests.get(urls, headers=headers)
        html = rsp.content.decode('ISO-8859-1')
        # 通过BeautifulSoup，来解析html页面
        soup = BeautifulSoup(html)
        # 通过分析我们发现数据在　id为ip_list的table标签中的tr标签中
        trs = soup.find_all(name='tr')  # 这里获得的是一个list列表
        print(trs)
        # 我们循环这个列表
        for item in trs[1:]:
            # 并至少出每个tr中的所有td标签
            tds = item.find_all('td')
            # 我们会发现有些img标签里面是空的，所以这里我们需要加一个判断
            if tds[0].text.strip() == 'ip':
                continue
            # 通过td列表里面的数据，我们分别把它们提取出来
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            # 将获取到的数据按照规定格式写入txt文本中，这样方便我们获取
            proxyIpDatas.append({"ip": ip, "port": port})
    return proxyIpDatas


def verifyProxyList(proxyIpDatas):
    verifiedIpDatas = []
    for proxyIpItem in proxyIpDatas:
        ip = proxyIpItem["ip"]
        port = proxyIpItem["port"]
        realip = ip + ':' + port
        code = verifyProxy(realip)
        if code == 200:
            print("---Success:" + ip + ":" + port)
            verifiedIpDatas.append(realip)
        else:
            print("---Failure:" + ip + ":" + port)
    return verifiedIpDatas


def verifyProxy(ip):
    '''
    验证代理的有效性
    '''
    herder = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Upgrade-Insecure-Requests': '1'
    }
    url = 'https://www.baidu.com'
    proxies = {"http": "http://" + str(ip)}
    request = requests.get(url, headers=herder, proxies=proxies)
    return request.status_code


verifiedIpDatas = []


def getVerifiedIp():
    """
    获取有效的代理ip
    """
    global verifiedIpDatas
    if len(verifiedIpDatas) == 0:
        # proxyIpDatas = getProxy("http://www.xicidaili.com/nn/")
        proxyIpDatas = getProxy("http://www.xicidaili.com/nt/")
        # getProxy("http://www.xicidaili.com/wn/")
        # getProxy("http://www.xicidaili.com/wt/")
        verifiedIpDatas = verifyProxyList(proxyIpDatas)
    ipAddress = ""
    if len(verifiedIpDatas) > 0:
        index = random.randint(0, len(verifiedIpDatas))
        if index < len(verifiedIpDatas):
            ipAddress = verifiedIpDatas[index]

    return ipAddress


def delVerifiedIp(ip):
    global verifiedIpDatas
    if len(ip) > 0:
        verifiedIpDatas.remove(ip)


#getVerifiedIp();
