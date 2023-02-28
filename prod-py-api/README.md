## 建立Dict 不用list append的方式新增資料
```py
for Resource_id in Ubike_Resource:
        Dict[count] = {}
        Dict[count]['場站'] = str(Ubike_Resource[Resource_id]['sna'])
        Dict[count]['場站總停車格'] = str(Ubike_Resource[Resource_id]['tot'])
        Dict[count]['場站目前車輛數量'] = str(Ubike_Resource[Resource_id]['sbi'])
        Dict[count]['空位數量'] = str(Ubike_Resource[Resource_id]['bemp'])
        Dict[count]['場站來源資料更新時間'] = str(Ubike_Resource[Resource_id]['mday'])
        count += 1
```
## 注意 SQL格式化後 回到 py Table 命名 有大小寫區別
```py
if (results[0] != 1):
    sql = "CREATE TABLE log( UUID VARCHAR(40), address VARCHAR(20), search_way VARCHAR(20), search_str VARCHAR(100), result MEDIUMTEXT, search_time DATETIME,result_json json , PRIMARY KEY(UUID) )"
    try:
        cursor.execute(sql)
    except:
        db.rollback()
```


## 忽略pip警告 
#### https://bobbyhadz.com/blog/python-warning-running-pip-as-the-root-user-can-result-in-broken-permissions
## docker containers-image-volumes-networks 移除。中間卡了大半時間在刪除image
#### https://blog.clarence.tw/2019/09/10/docker-removing-containers-images-volumes-and-networks/
