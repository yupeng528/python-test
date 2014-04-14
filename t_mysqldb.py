#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 yupeng <yupeng@yupengtekiMacBook-Air.local>
#
# Distributed under terms of the MIT license.

"""
test mysqlsdb
"""
import MySQLdb


#连接
conn=MySQLdb.connect(host="localhost",user="root",passwd="sa123",db="nodejs",charset="utf8")
cursor = conn.cursor()

#写入
sql = "insert into t_user(name) values(%s)"
param = ("fff")
n = cursor.execute(sql,param)
conn.commit()
print n

#查询
n = cursor.execute("select * from t_user")
for row in cursor.fetchall():
    for r in row:
        print r


#更新
sql = "update t_user set name=%s where id=3"
param = ("yupeng")
n = cursor.execute(sql,param)
conn.commit()
print n


#删除
sql = "delete from t_user where name=%s"
param =("eee")
n = cursor.execute(sql,param)
conn.commit()
print n
cursor.close()

#关闭
conn.close()
