#coding=utf-8
from __future__ import with_statement
from fabric.api import local, env, settings, abort, run, cd, lcd
from fabric.contrib.console import confirm
import time

env.hosts = ['60.205.216.128:5711']
env.user = 'root'
env.key_filename = 'C:\Users\mac\Documents\id_rsa_mopyfish'

def push():
    local("git add .")
    local("git commit")
    local("git push")

def update_server():
    with cd("/home/cg/jobboard.worker"):
        run('git checkout .') 
        run('git pull') 
        run('chmod 777 *')
        run('supervisorctl restart jobboard.worker')
	
def deploy():
	push()
	update_server()
	
