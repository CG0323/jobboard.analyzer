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
    text_file = open("all.txt", "w")
    contents = get_all_contents()
    skills = get_all_skills()
    total = len(contents)
    i = 0
    for content in contents:
        i = i + 1
        print "handle " + str(i) + "/" + str(total) 
        lines = content['Text'].split('\n')
        for line in lines:
            keep = False
            for skill in skills:
                if detect_skill(line, skill) == True and "developer" not in line:
                    keep = True
                    break
                if detect_keepsigns(line) == True:
                    keep = True
                    break
            if keep == True:
                line = line.replace("*","")
                text_file.write(line.encode('utf8'))
                
    text_file.close()
                

if __name__=='__main__':
    process_all_contents()