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

def get_all_contents():
    connection = get_connection()
    contents = []
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Content"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results 
    connection.close()



def add_job_skills(job_id, skill_ids):
    connection = get_connection()
    try:
        print "add skill for job_id = " + str(job_id) + " : " + ",".join(skill_ids)
        with connection.cursor() as cursor:
            sql = "INSERT IGNORE INTO JobSkill (JobId,SkillId) VALUES(%s,%s)"
            for skill_id in skill_ids:
                data = (job_id, skill_id)
                cursor.execute(sql, data)
            connection.commit()
    finally:
        connection.close()