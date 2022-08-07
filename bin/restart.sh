# !/bin/bash

# 先杀死旧的进程
ps -ef | grep python3 | cut -c 9-15 | xargs kill -9

# 迁移数据库
python3 manage.py makemigrations
python3 manage.py migrate

# 启动
nohup python3 manage.py runserver 0.0.0.0:80 > logs/log.log 2>&1 &