# Youbike_API
 devolope the API for Search Ubike information

>Set up sever on AWS (EC2 type:t2.small storage 16GB) and use docker-compose deploye myslq、flask. Also install UI phpmyadmin、adminer and coding enviromen VSC. Network use nginx achieve reverse proxy

## URL:https://web.54.144.132.96.nip.io/
#### DB
### https://phpmyadmin.54.144.132.96.nip.io/index.php?route=/sql&pos=0&db=youbike&table=log 
#### VSC
### https://vscode.54.144.132.96.nip.io/?folder=/home/coder 

## Youbike API 使用方法
### allInfo GET : 取得全部場站資料
#### https://web.54.144.132.96.nip.io/allInfo
### allInfo/json GET : 取得全部場站資料JSON
#### https://web.54.144.132.96.nip.io/allInfo/json
### snaSearch POST : BODY key in 搜尋的場站，取得場站資料
#### https://web.54.144.132.96.nip.io/snaSearch
### snaSearch/json POST : BODY key in 搜尋的場站，取得場站資料JSON
#### https://web.54.144.132.96.nip.io/snaSearch/json
![This is an image](https://github.com/jayger1132/py_API/blob/main/post_eg.png)

## 參考
#### https://github.com/hsuanchi/flask-template
### EC2實作
#### https://www.youtube.com/watch?v=SgSnz7kW-Ko
