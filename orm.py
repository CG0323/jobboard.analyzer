#!./env/bin/python
import pymysql.cursors
import pymysql as my
import time
import sys

def get_connection():
    connection = pymysql.connect(host='localhost',
                                    user='cg',
                                    password='123456',
                                    db='jobboard',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
    return connection

def get_all_skills():
    connection = get_connection()
    skills = []
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Skill"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results 
    connection.close()
    