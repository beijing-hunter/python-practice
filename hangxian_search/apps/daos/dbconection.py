import pymysql


def dbConnection():
    try:
        con = pymysql.connect(host="127.0.0.1", user="root", password="123456", database="hangxian_search",
                              charset='utf8', port=3306)
    except Exception as e:
        print(e)
    finally:
        return con
