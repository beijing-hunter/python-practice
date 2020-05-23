import pymysql


def dbConnection():
    try:
        con = pymysql.connect(host="123.56.4.34", user="root", password="cmt123", database="cmt_spider", port=3306)
    except Exception as e:
        print(e)
    finally:
        return con


def addData(postInfo):
    con = dbConnection()
    cur = con.cursor()
    sql = "insert into cm_post(`title`,link_url,platform_id,platform_post_token,create_time,update_time,status) values(%s,%s,%s,%s,now(),now(),1)"
    try:
        result = cur.execute(sql, (
            postInfo["title"], postInfo["linkUrl"], postInfo["platformId"], postInfo["platformPostToken"]))
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
    finally:
        con.close()


def findOne(platformId, platformPostToken):
    """
    查询咨询信息
    :param platformId:
    :param platformPostToken:
    :return:
    """
    con = dbConnection()
    cur = con.cursor()
    postInfo = {}
    count = 0  # 是否查询到数据

    try:
        sql = "select id,title,link_url,platform_id,platform_post_token from cm_post where platform_id=%s and platform_post_token=%s"
        rows = cur.execute(sql, (platformId, platformPostToken))
        result = cur.fetchone()

        if rows > 0 and len(result) > 0:
            postInfo = {"id": result[0], "title": result[1], "linkUrl": result[2], "platformId": result[3],
                        "platformPostToken": result[4]}
            count = 1
    except Exception as e:
        print(e)
    finally:
        con.close()
        return postInfo, count

def findAll():
    con = dbConnection()
    cur = con.cursor()
    postInfos = []

    try:
        sql = "select id,title,link_url,platform_id,platform_post_token from cm_post where status=1"
        cur.execute(sql)
        result = cur.fetchall()
        if len(result) > 0:
            for item in result:
                postInfo = {"id": item[0], "title": item[1], "linkUrl": item[2], "platformId": item[3],
                            "platformPostToken": item[4]}
                postInfos.append(postInfo)
    except Exception as e:
        print(e)
    finally:
        con.close()
        return postInfos


def updateInfo(postInfo):
    con = dbConnection()
    cur = con.cursor()

    try:
        sql = "update cm_post set status=%s,in_keys=%s where id=%s"
        cur.execute(sql, (postInfo["status"],postInfo["inKeys"],postInfo["id"]))
        con.commit()
    except Exception as e:
        print(e)
        con.rollback()
    finally:
        con.close()