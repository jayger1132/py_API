# py_API
 devolope the API for Search Ubike information
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
