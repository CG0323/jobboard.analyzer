#!./env/bin/python
from orm import *
import re
import time

def detect_skill(content, skill):
    text = content["Text"]
    if skill["IsReg"] == True:
        pattern = re.compile(skill["Keywords"])
        match = pattern.search(text)
        if match:
            return True
        else:
            return False
    else:
        keywords = skill["KeyWords"].split(",")
        for keyword in keywords:
            if keyword in text:
                return True
        return False

def analyze_all_job_all_skill():
    contents = get_all_contents()
    skills = get_all_skills()
    for content in contents:
        print "====================================="
        print "anaylze job id = " + str(content["JobId"])
        skill_ids = []
        for skill in skills:
            if detect_skill(content, skill) == True:
                print "skill detected = " + skill["Name"]
                skill_ids.append(skill["Id"])
        if len(skill_ids) > 0:
            add_job_skills(content["JobId"], skill_ids)

def analyze_all_job_one_skill(skill_id):
    contents = get_all_contents()
    skill = get_skill(skill_id)
    for content in contents:
        print "====================================="
        print "anaylze job id = " + str(content["JobId"])
        skill_ids = []
        if detect_skill(content, skill) == True:
            print "skill detected = " + skill["Name"]
            skill_ids.append(skill["Id"])
        if len(skill_ids) > 0:
            add_job_skills(content["JobId"], skill_ids)

def analyze_one_job_all_skill(job_id):
    content = get_content(job_id)
    skills = get_all_skills()
    print "====================================="
    print "anaylze job id = " + str(content["JobId"])
    skill_ids = []
    for skill in skills:
        if detect_skill(content, skill) == True:
            print "skill detected = " + skill["Name"]
            skill_ids.append(skill["Id"])
    if len(skill_ids) > 0:
        add_job_skills(content["JobId"], skill_ids)   

if __name__=='__main__':
    analyze_all_job_all_skill()