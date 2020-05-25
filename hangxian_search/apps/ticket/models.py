from django.db import models
from apps.daos import dbconection


# Create your models here.
class Ticket():
    def __init__(self):
        self.airlineName = ""
        self.flightNumber = ""
        self.departureDate = ""
        self.departureDatetime = ""
        self.arrivalDate = ""
        self.arrivalDatetime = ""
        self.departureCityName = ""
        self.departureAirportName = ""
        self.arrivalCityName = ""
        self.arrivalAirportName = ""
        self.printprice = ""
        self.id = 0.00


class SearchRecord():
    def __init__(self):
        self.id = 0
        self.userId = 0
        self.searchKey = ""


class HotSail():
    def __init__(self):
        self.hotSailContent = ""
        self.hotCount = 0


def findInfos(searchKey, departureDate):
    """
    根据搜索信息，查询航班信息
    """
    con = dbconection.dbConnection()
    cur = con.cursor()
    datas = []
    dIndex = searchKey.find("到")

    try:
        sql = "select departureCityName,arrivalCityName,departureDate,departureDatetime,departureAirportName,arrivalDate,arrivalDatetime,arrivalAirportName,printprice,airlineName,flightNumber"

        if dIndex >= 0:
            sql = sql + " from ticket where" + (" departureDate=%s and " if len(departureDate) > 0 and departureDate != '-1' else "") + " departureCityName=%s and arrivalCityName=%s order by departureDate desc,departureDatetime"
            keys = searchKey.split("到")

            if len(departureDate)>0 and departureDate!='-1':
                cur.execute(sql, (departureDate,keys[0].strip(), keys[1].strip()))
            else:
                cur.execute(sql, (keys[0].strip(), keys[1].strip()))
        else:
            sql = sql + " from ticket where "+ (" departureDate=%s and " if len(departureDate) > 0 and departureDate != '-1' else "")+" (departureCityName=%s or arrivalCityName=%s) order by departureDate desc,departureDatetime"
            if len(departureDate) > 0 and departureDate != '-1':
                cur.execute(sql, (departureDate,searchKey, searchKey))
            else:
                cur.execute(sql, (searchKey, searchKey))
        result = cur.fetchall()
        if len(result) > 0:
            for item in result:
                info = Ticket()
                info.departureCityName = item[0]
                info.arrivalCityName = item[1]
                info.departureDate = item[2]
                info.departureDatetime = item[3]
                info.departureAirportName = item[4]
                info.arrivalDate = item[5]
                info.arrivalDatetime = item[6]
                info.arrivalAirportName = item[7]
                info.printprice = item[8]
                info.airlineName = item[9]
                info.flightNumber = item[10]
                datas.append(info)
    except Exception as e:
        print(e)
    finally:
        con.close()
        return datas


def addSearchRecord(userId, searchKey):
    """
    添加用户搜索记录
    :param userId:
    :param searchKey:
    :return:
    """
    con = dbconection.dbConnection()
    cur = con.cursor()
    sql = "insert into search_record(userId,searchKey) values(%s,%s)"
    try:
        result = cur.execute(sql, (userId, searchKey))
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
    finally:
        con.close()
        return cur.lastrowid


def findSearchRecrods(userId):
    """
    查询用户搜索历史记录
    :param userId:
    :return:
    """
    con = dbconection.dbConnection()
    cur = con.cursor()
    datas = []

    try:
        sql = "SELECT DISTINCT searchKey FROM search_record WHERE userId=%s ORDER BY id DESC LIMIT 20"
        cur.execute(sql, (userId,))
        result = cur.fetchall()
        if len(result) > 0:
            for item in result:
                info = SearchRecord()
                info.searchKey = item[0]
                datas.append(info)
    except Exception as e:
        print(e)
    finally:
        con.close()
        return datas


def addHotSail(searchKey):
    """
    添加热门航线
    :param searchKey:
    :return:
    """
    con = dbconection.dbConnection()
    cur = con.cursor()
    sql = "insert into hot_sail(hot_sail_content) values(%s)"
    try:
        result = cur.execute(sql, (searchKey,))
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
    finally:
        con.close()
        return cur.lastrowid


def findHotSail():
    """
    查询热门航线
    :param userId:
    :return:
    """
    con = dbconection.dbConnection()
    cur = con.cursor()
    datas = []

    try:
        sql = "SELECT DISTINCT hot_sail_content,count(1) as hotCount FROM hot_sail GROUP BY hot_sail_content having hotCount>=10 ORDER BY hotCount desc LIMIT 10"
        cur.execute(sql)
        result = cur.fetchall()
        if len(result) > 0:
            for item in result:
                info = HotSail()
                info.hotSailContent = item[0]
                info.hotCount = item[1]
                datas.append(info)
    except Exception as e:
        print(e)
    finally:
        con.close()
        return datas


def findDepartureDate():
    """
    查询出发日期
    :param userId:
    :return:
    """
    con = dbconection.dbConnection()
    cur = con.cursor()
    datas = []

    try:
        sql = "SELECT departureDate FROM ticket GROUP BY departureDate ORDER BY departureDate desc"
        cur.execute(sql)
        result = cur.fetchall()
        if len(result) > 0:
            for item in result:
                datas.append({"departureDate": item[0]})
    except Exception as e:
        print(e)
    finally:
        con.close()
        return datas
