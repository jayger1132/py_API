import pymysql
from datetime import datetime, timedelta
dbhost = '127.0.0.1'
dbport = 3306
dbuser = 'root'
dbpass = 'tokio328'
dbname = 'youbike'
try:
    db = pymysql.connect(host=dbhost, user=dbuser,
                         port=dbport, password=dbpass, database=dbname)
    print("連結成功")
    cursor = db.cursor()
except pymysql.Error as e:
    print("連線失敗"+str(e))
    # 如果資料表不存在，則新增資料表
sql = "SELECT COUNT(1) FROM information_schema.tables WHERE table_schema='youbike' AND table_name = 'log';"
try:
    cursor.execute(sql)
    results = cursor.fetchone()
except:
    db.rollback()

if (results[0] != 1):
    sql = "CREATE TABLE LOG( UUID INT AUTO_INCREMENT, Address VARCHAR(20), search_way VARCHAR(20), search_str VARCHAR(100), result MEDIUMTEXT, search_time DATETIME, PRIMARY KEY(UUID) )"
    try:
        cursor.execute(sql)
    except:
        db.rollback()


def INSERT(ip,string):
    print(ip)
    return string


def UPDATE():
    return
