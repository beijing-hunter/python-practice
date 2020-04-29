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


def findInfos(searchKey):
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
            sql = sql + " from ticket where departureCityName=%s and arrivalCityName=%s order by departureDate,departureDatetime"
            keys = searchKey.split("到")
            cur.execute(sql, (keys[0].strip(), keys[1].strip()))
        else:
            sql = sql + " from ticket where departureCityName=%s or arrivalCityName=%s order by departureDate,departureDatetime"
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
