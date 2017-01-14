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


def add_job_skills(job_id, skills_with_level):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT IGNORE INTO JobSkill (JobId,SkillId,Level) VALUES(%s,%s,%s)"
            for skill in skills_with_level:
                data = (job_id, skill["id"], skill["level"])
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

def clear_all_from_job_skill_table():
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "DELETE FROM JobSkill" 
        cursor.execute(sql)
        connection.commit()
    connection.close()