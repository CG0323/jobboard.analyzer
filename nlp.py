#!./env/bin/python
from orm import *
import re
import time

keepsigns = ["degree","master","bachelor","computer science","university","diploma","desired", "desirable","bonus","nice to have", "must have", "mandotory","preferred"]

def detect_skill(line, skill):
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

def detect_keepsigns(line):
    for keepsign in keepsigns:
            if keepsign in line:
                return True
    return False

def process_all_contents():
    contents = get_all_contents()
    skills = get_all_skills()
    for content in contents:
        lines = content['Text'].split('\n')
        for line in lines:
            keep = False
            for skill in skills:
                if detect_skill(line, skill) == True:
                    keep = True
                    break
                if detect_keepsigns(line) == True:
                    keep = True
                    break
            if keep == True:
                print line
                time.sleep(2)
        




if __name__=='__main__':
    process_all_contents()