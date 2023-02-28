import pymysql
import time
import uuid
dbhost = '54.144.132.96'
dbport = 3306
dbuser = 'jayger1132'
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
    sql = "CREATE TABLE LOG( UUID VARCHAR(40), address VARCHAR(20), search_way VARCHAR(20), search_str VARCHAR(100), result MEDIUMTEXT, search_time DATETIME,result_json json , PRIMARY KEY(UUID) )"
    try:
        cursor.execute(sql)
    except:
        db.rollback()


def INSERT(ip, search_way, search_str, result):
    # 創建uuid 根據日期、時間與網路卡的 MAC 位址所產生
    myuuid = uuid.uuid1()
    print(str(search_str), search_way)
    current_time = time.strftime(
        '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    sql = "INSERT INTO log(UUID,address,search_way,search_str,result,search_time) VALUES ('%s' , '%s' ,'%s' , '%s' ,'%s' , '%s')" % (
        myuuid, ip, search_way, search_str, result, current_time)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


def INSERT_json(ip, search_way, search_str, result_json):
    myuuid = uuid.uuid1()
    current_time = time.strftime(
        '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    sql = "INSERT INTO log(UUID,address,search_way,search_str,result_json,search_time) VALUES ('%s' , '%s' ,'%s' , '%s' ,'%s' , '%s')" % (
        myuuid, ip, search_way, search_str, result_json, current_time)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
