#!./env/bin/python
from orm import *
import re
import time
import logging

logger = logging.getLogger("worker")
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def detect_skill(content, skill):
    text = content["Text"]
    logger.debug(skill)
    if skill["IsReg"] == 1:
        pattern = re.compile(skill["KeyWords"])
        logger.info("I am here")
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
        skill_ids = []
        for skill in skills:
            if detect_skill(content, skill) == True:
                print "skill detected = " + skill["Name"]
                skill_ids.append(skill["Id"])
        if len(skill_ids) > 0:
            add_job_skills(content["JobId"], skill_ids)

def analyze_all_job_one_skill(skill_id):
    logger.info("analyze all jobs for skill id = %s", skill_id)
    sys.stdout.flush()
    clear_from_job_skill_table(skill_id)
    contents = get_all_contents()
    skill = get_skill(skill_id)
    logger.info(skill)
    for content in contents:
        skill_ids = []
        if detect_skill(content, skill) == True:
            # print "skill detected = " + skill["Name"]
            skill_ids.append(skill["Id"])
        if len(skill_ids) > 0:
            add_job_skills(content["JobId"], skill_ids)

def analyze_one_job_all_skill(job_id):
    logger.info("analyze job id = %s for all skills", job_id)
    sys.stdout.flush()
    content = get_content(job_id)
    skills = get_all_skills()
    skill_ids = []
    for skill in skills:
        if detect_skill(content, skill) == True:
            skill_ids.append(skill["Id"])
    if len(skill_ids) > 0:
        add_job_skills(content["JobId"], skill_ids)   

def clean_skill(skill_id):
    logger.info("clean JobSkill for skill id = %s", skill_id)
    sys.stdout.flush()
    clear_from_job_skill_table(skill_id)

if __name__=='__main__':
    # analyze_all_job_all_skill()
    analyze_all_job_one_skill(84)