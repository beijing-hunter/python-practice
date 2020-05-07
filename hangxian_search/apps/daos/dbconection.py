import pymysql


def dbConnection():
    try:
        con = pymysql.connect(host="192.168.199.88", user="root", password="root", database="hangxian_search",
                              charset='utf8', port=3306)
    except Exception as e:
        print(e)
    finally:
        return con
