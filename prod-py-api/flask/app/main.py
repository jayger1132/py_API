# coding:utf-8
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import numpy as np
from sql import *

# 開發搜尋場站API
# 查詢全部場站資訊API
app = Flask(__name__)
CORS(app)


@app.route("/allInfo", methods=['GET'])
def GET_All():
    # 取得IP
    # ip = request.remote_addr
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    with requests.get("https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json") as response:
        Ubike_Resource = response.json()
        Ubike_Resource = Ubike_Resource['retVal']
    Result = ''
    # 搜尋所有場站資料

    for Resource_id in Ubike_Resource:
        Result += ('場站: '+str(Ubike_Resource[Resource_id]['sna']) +
                   ' 場站總停車格: '+str(Ubike_Resource[Resource_id]['tot']) +
                   ' 場站目前車輛數量: '+str(Ubike_Resource[Resource_id]['sbi']) +
                   ' 空位數量: '+str(Ubike_Resource[Resource_id]['bemp']) +
                   ' 場站來源資料更新時間: '+str(Ubike_Resource[Resource_id]['mday'])+'\n')
    INSERT(ip, 'AllInfo', 'NULL', Result)
    return Result, 200


@app.route('/allInfo/json', methods=['GET'])
def GET_All_json():
    import json
    ip = request.remote_addr
    with requests.get('https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json') as response:
        Ubike_Resource = response.json()
        Ubike_Resource = Ubike_Resource['retVal']
    Dict = {}
    count = 0
    # nested dict 建立
    for Resource_id in Ubike_Resource:
        Dict[count] = {}
        Dict[count]['場站'] = str(Ubike_Resource[Resource_id]['sna'])
        Dict[count]['場站總停車格'] = str(Ubike_Resource[Resource_id]['tot'])
        Dict[count]['場站目前車輛數量'] = str(Ubike_Resource[Resource_id]['sbi'])
        Dict[count]['空位數量'] = str(Ubike_Resource[Resource_id]['bemp'])
        Dict[count]['場站來源資料更新時間'] = str(Ubike_Resource[Resource_id]['mday'])
        count += 1
    # dump v.s dumps 差異在有無存入文件  dump有
    # 原先的格式是用dict 所以在存入sql會有格式上的出錯
    Dict_sql = json.dumps(Dict, ensure_ascii=False)
    INSERT_json(ip, 'AllInfo', 'NULL', Dict_sql)
    return {'result': Dict}, 200

# 直接將搜尋資料輸入在URL
# @app.route('/sna/<string:name>', methods=['POST'])
# def post_sna(name):
#     return name


@app.route('/snaSearch', methods=['POST'])
def POST_sna():
    ip = request.remote_addr
    input = str(request.get_data(), 'utf-8')
    input_Resource = str(request.get_data(), 'utf-8')
    print(input_Resource)
    with requests.get('https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json') as response:
        Ubike_Resource = response.json()
        Ubike_Resource = Ubike_Resource['retVal']
    input = str(input_Resource).split(' ')
    sna_arrs = []
    Result = ''
    for Resource_id in Ubike_Resource:
        for temp in input:
            if temp in Ubike_Resource[Resource_id]['sna']:
                # 如果已經被記錄過，則略過。
                if str(Ubike_Resource[Resource_id]['sna']) in sna_arrs:
                    None
                else:
                    sna_arrs.append(str(Ubike_Resource[Resource_id]['sna']))
                    Result += ('場站: '+str(Ubike_Resource[Resource_id]['sna']) +
                               ' 場站總停車格: '+str(Ubike_Resource[Resource_id]['tot']) +
                               ' 場站目前車輛數量: '+str(Ubike_Resource[Resource_id]['sbi']) +
                               ' 空位數量: '+str(Ubike_Resource[Resource_id]['bemp']) +
                               ' 場站來源資料更新時間: '+str(Ubike_Resource[Resource_id]['mday'])+'\n')
    INSERT(ip, 'snaSearch', input_Resource, Result)
    return Result, 200


@app.route('/snaSearch/json', methods=['POST'])
def POST_sna_json():
    import json
    input_Resource = str(request.get_data(), 'utf-8')
    print(input_Resource)
    ip = request.remote_addr
    with requests.get('https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json') as response:
        Ubike_Resource = response.json()
        Ubike_Resource = Ubike_Resource['retVal']
    input = str(input_Resource).split(' ')
    sna_Dict = {}
    count = 0
    for Resource_id in Ubike_Resource:
        for temp in input:
            if temp in Ubike_Resource[Resource_id]['sna']:
                # 如果已經被記錄過，則略過。
                if str(Ubike_Resource[Resource_id]['sna']) in sna_Dict.values():
                    None
                else:
                    sna_Dict[count] = {}
                    sna_Dict[count]['場站'] = str(
                        Ubike_Resource[Resource_id]['sna'])
                    sna_Dict[count]['場站總停車格'] = str(
                        Ubike_Resource[Resource_id]['tot'])
                    sna_Dict[count]['場站目前車輛數量'] = str(
                        Ubike_Resource[Resource_id]['sbi'])
                    sna_Dict[count]['空位數量'] = str(
                        Ubike_Resource[Resource_id]['bemp'])
                    sna_Dict[count]['場站來源資料更新時間'] = str(
                        Ubike_Resource[Resource_id]['mday'])
                    count += 1
    sna_Dict_sql = json.dumps(sna_Dict, ensure_ascii=False)
    INSERT_json(ip, 'snaSearch', input_Resource, sna_Dict_sql)
    return {'result': sna_Dict}, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
