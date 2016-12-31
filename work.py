#!./env/bin/python
from orm import *
import re
import time

def detect_skill(content, skill):
    text = content["Text"]
    if skill["IsReg"] is True:
        print "reg is true"
        pattern = re.compile(skill["Keywords"])
        match = pattern.search(text)
        if match:
            return True
        else:
            return False
    else:
        print "reg is false"
        keywords = skill["KeyWords"].split(",")
        print keywords
        for keyword in keywords:
            if keyword in text:
                return True
        return False

def analyze_all_job_all_skill():
    contents = get_all_contents()
    skills = get_all_skills()
    for content in contents:
        time.sleep(5)
        print "====================================="
        print "anaylze job id = " + str(content["JobId"])
        skill_ids = []
        for skill in skills:
            if detect_skill(content, skill):
                print "skill detected = " + skill["Name"]
                skill_ids.append(skill["Id"])
        if len(skill_ids) > 0:
            add_job_skills(content["JobId"], skill_ids)

if __name__=='__main__':
    analyze_all_job_all_skill()
