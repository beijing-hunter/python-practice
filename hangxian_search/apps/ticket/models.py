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
        self.departureCity = ""
        self.arrivalCity = ""


class HotSail():
    def __init__(self):
        self.hotSailContent = ""
        self.hotCount = 0
        self.departureCity = ""
        self.arrivalCity = ""


def findInfos(departureCity, arrivalCity, departureDate):
    """
    根据搜索信息，查询航班信息
    """
    con = dbconection.dbConnection()
    cur = con.cursor()
    datas = []
    sqlParam = []

    try:
        sql = "select departureCityName,arrivalCityName,departureDate,departureDatetime,departureAirportName,arrivalDate,arrivalDatetime,arrivalAirportName,printprice,airlineName,flightNumber"
        sql = sql + " from ticket where 1=1 "

        if len(departureDate) > 0 and departureDate != '-1':
            sqlParam.append(departureDate)
            sql = sql + " and departureDate=%s  "
        if len(departureCity) > 0:
            sql = sql + " and departureCityName=%s "
            sqlParam.append(departureCity.strip())
        if len(arrivalCity) > 0:
            sql = sql + " and arrivalCityName=%s "
            sqlParam.append(arrivalCity)
        sql = sql + "   order by departureDate desc,departureDatetime "

        if len(sqlParam) > 0:
            cur.execute(sql, tuple(sqlParam))
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


def addSearchRecord(userId, departureCity, arrivalCity):
    """
    添加用户搜索记录
    :param userId:
    :param searchKey:
    :return:
    """
    con = dbconection.dbConnection()
    cur = con.cursor()
    sql = "insert into search_record(userId,departureCity,arrivalCity) values(%s,%s,%s)"
    try:
        result = cur.execute(sql, (userId, departureCity, arrivalCity))
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
        sql = "SELECT DISTINCT departureCity,arrivalCity FROM search_record WHERE userId=%s ORDER BY id DESC LIMIT 20"
        cur.execute(sql, (userId,))
        result = cur.fetchall()
        if len(result) > 0:
            for item in result:
                info = SearchRecord()
                info.departureCity = item[0]
                info.arrivalCity = item[1]
                datas.append(info)
    except Exception as e:
        print(e)
    finally:
        con.close()
        return datas


def addHotSail(departureCity, arrivalCity):
    """
    添加热门航线
    :param searchKey:
    :return:
    """
    con = dbconection.dbConnection()
    cur = con.cursor()
    sql = "insert into hot_sail(hot_sail_content) values(%s)"
    try:
        result = cur.execute(sql, (departureCity + "到" + arrivalCity))
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
                keys = info.hotSailContent.split("到")
                info.hotCount = item[1]
                info.departureCity = keys[0]
                info.arrivalCity = keys[1]
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
