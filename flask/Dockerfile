# FROM python:alpine
# Use the Python3.7.2 image
# 指定一個 image 來源
FROM python:3.9-slim
WORKDIR /app
ADD . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install the dependencies
# build 時使用，會執行此命令
RUN pip install --upgrade pip
RUN pip install --root-user-action=ignore requests
RUN pip install -r requirements.txt

# run the command to start uWSGI
# run container 時要執行的命令
CMD ["uwsgi", "app.ini"]