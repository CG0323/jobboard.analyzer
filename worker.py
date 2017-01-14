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

LEVEL3_KEYWORDS = ["excellent", "demonstrated", "solid", "strong", "proven", "in-depth", "years", "extensive", "proficent"]
LEVEL2_KEYWORDS = ["good", "experience", "knowledge", "familiar", "familiarity"]
LEVEL1_KEYWORDS = ["asset", "nice to have", "optional", "plus", "bonus", "not mandatory"]

def detect_skill_in_line(line, skill):
    if skill["IsReg"] == '\x01':
        pattern = re.compile(skill["KeyWords"])
        match = pattern.search(line)
        if match:
            return True
        else:
            return False
    else:
        keywords = skill["KeyWords"].split(",")
        for keyword in keywords:
            if keyword in line:
                return True
        return False

def get_required_level(line):
    for keyword in LEVEL3_KEYWORDS:
        if keyword in line:
            return 3
    for keyword in LEVEL1_KEYWORDS:
        if keyword in line:
            return 1
    return 2

def analyze_skill(content, skill):
    text = content["Text"]
    lines = text.split('\n')
    for line in lines:
        if detect_skill_in_line(line,skill) == True:
            return get_required_level(line)
    return 0

def analyze_all_job_all_skill():
    clear_all_from_job_skill_table()
    contents = get_all_contents()
    skills = get_all_skills()
    for content in contents:
        skills_with_level = []
        for skill in skills:
            required_level = analyze_skill(content, skill)
            if required_level > 0:
                print "skill detected = " + skill["Name"] + ", require level " + str(required_level)
                skills_with_level.append({"id":skill["Id"],"level":required_level})
        if len(skills_with_level) > 0:
            add_job_skills(content["JobId"], skills_with_level)

def analyze_all_job_one_skill(skill_id):
    logger.info("analyze all jobs for skill id = %s", skill_id)
    sys.stdout.flush()
    clear_from_job_skill_table(skill_id)
    contents = get_all_contents()
    skill = get_skill(skill_id)
    for content in contents:
        skills_with_level = []
        required_level = analyze_skill(content, skill)
        if required_level > 0:
            print "skill detected = " + skill["Name"] + ", require level " + str(required_level)
            skills_with_level.append({"id":skill["Id"],"level":required_level})
        if len(skills_with_level) > 0:
            add_job_skills(content["JobId"], skills_with_level)

def analyze_one_job_all_skill(job_id):
    logger.info("analyze job id = %s for all skills", job_id)
    sys.stdout.flush()
    content = get_content(job_id)
    skills = get_all_skills()
    skills_with_level = []
    for skill in skills:
        required_level = analyze_skill(content, skill)
        if required_level > 0:
            print "skill detected = " + skill["Name"] + ", require level " + str(required_level)
            skills_with_level.append({"id":skill["Id"],"level":required_level})
    if len(skills_with_level) > 0:
        add_job_skills(content["JobId"], skills_with_level)   

def clean_skill(skill_id):
    logger.info("clean JobSkill for skill id = %s", skill_id)
    sys.stdout.flush()
    clear_from_job_skill_table(skill_id)

if __name__=='__main__':
    analyze_all_job_all_skill()