import pymysql

def dbConnection():
    try:
        con = pymysql.connect(host="localhost", user="root", password="123456", database="onlinekq", port=3306)
    except Exception as e:
        print(e)
    finally:
        return con

def addData():
    con = dbConnection()
    cur = con.cursor()
    sql = "insert into bank(`number`,pay,pwd) values(%s,%s,%s)"
    try:
        result = cur.execute(sql, (23, 23.4, "12345"))
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
    finally:
        con.close()


def addDataBatch():
    con = dbConnection()
    cur = con.cursor()
    sql = "insert into bank(`number`,pay,pwd) values(%s,%s,%s)"
    try:
        executCount = cur.executemany(sql, [(24, 23.4, "12345"), (25, 45.3, "12345")])
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
    finally:
        con.close()


def findOne(number):
    con = dbConnection()
    cur = con.cursor()
    bankInfo = {}

    try:
        sql = "select * from bank where number=%s"
        cur.execute(sql, (number,))
        result = cur.fetchone()

        if len(result) > 0:
            bankInfo = {"number": result[0], "pay": result[1], "pwd": result[2]}
    except Exception as e:
        print(e)
    finally:
        con.close()
        return bankInfo


def findAll():
    con = dbConnection()
    cur = con.cursor()
    bankInfos = []

    try:
        sql = "select * from bank"
        cur.execute(sql)
        result = cur.fetchall()
        if len(result) > 0:
            for item in result:
                bankInfos.append({"number": item[0], "pay": item[1], "pwd": item[2]})
    except Exception as e:
        print(e)
    finally:
        con.close()
        return bankInfos


def updateInfo(number, pay):
    con = dbConnection()
    cur = con.cursor()

    try:
        sql = "update bank set pay=%s where number=%s"
        cur.execute(sql, (pay, number))
        con.commit()
    except Exception as e:
        print(e)
        con.rollback()
    finally:
        con.close()


def delInfo(number):
    con = dbConnection()
    cur = con.cursor()

    try:
        sql = "delete from bank where number=%s"
        cur.execute(sql, (number,))
        con.commit()
    except Exception as e:
        print(e)
        con.rollback()
    finally:
        con.close()