## Django
1. 新建一个Django项目，aisystem是项目名
```django-admin startproject aisystem```
2. 开启服务器
```python3 manage.py runserver```
3. 创建微服务（app），user是服务名
```python3 manage.py startapp user```
    + 在创建项目的时候本身就创建了一个和项目同名的微服务
    + 创建后应当的在setting.py里的INSTALLED_APPS里添加该app名
4. 创建映射（利用django生成表）
```python3 manage.py makemigrations [appname]```
    + appname理应不需要加，当新增app的时候，该命令会重新扫描所有setting.py里的INSTALLED_APPS列表
    + 如果无法识别列表有新增，则加上appname
5. 创建数据库
```python3 manage.py migrate```
    + pip3 install mysqlclient(pymysql)
    + 在创建前需要先在setting.py里DATABASES修改数据库引擎ENGINE，名称NAME，用户USER，密码PASSWORD，主机HOST，端口PORT

## 数据库mysql（注意末尾分号）
1. 进去mysql
```mysql -u root -p```
1. 显示所有的数据库
```show databases;```
2. 创建数据库，名称为aisystem
```create database aisystem;```
3. 进入数据库
```use aisystem;```
4. 查看当前的数据库
```select database();```
4. 查看表
```show tables;```
5. 查看表中属性，表名为user_tuser
```desc user_tuser;```