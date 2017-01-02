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
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Skill"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results 
    connection.close()

def get_skill(skill_id):
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Skill WHERE Id =%s" 
        cursor.execute(sql,(skill_id,))
        results = cursor.fetchall()
        return results[0] 
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

def get_content(job_id):
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Content WHERE JobId =%s" 
        cursor.execute(sql,(job_id,))
        results = cursor.fetchall()
        return results[0] 
    connection.close()


def add_job_skills(job_id, skill_ids):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT IGNORE INTO JobSkill (JobId,SkillId) VALUES(%s,%s)"
            for skill_id in skill_ids:
                data = (job_id, skill_id)
                cursor.execute(sql, data)
            connection.commit()
    finally:
        connection.close()

def clear_from_job_skill_table(skill_id):
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "DELETE FROM JobSkill WHERE SkillId =%s" 
        cursor.execute(sql,(skill_id,))
        connection.commit()
    connection.close()