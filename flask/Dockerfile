# FROM python:alpine
# Use the Python3.7.2 image
# 指定一個 image 來源
FROM python:3.9-slim
WORKDIR /app
ADD . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt