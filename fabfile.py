#coding=utf-8
from __future__ import with_statement
from fabric.api import local, env, settings, abort, run, cd, lcd
from fabric.contrib.console import confirm
import time

# env.use_ssh_config = True
env.hosts = ['60.205.216.128:5711']
env.user = 'root'
env.key_filename = 'C:\Users\mac\Documents\id_rsa_mopyfish'

def push():
    local("git add .")
    local("git commit -m 'auto_update'")
    local("git push")

def update_server():
    with cd("/home/cg/jobboard.worker"):
        run('git pull') 
        run('chmod 777 -R .')
	
def deploy():
	push()
	update_server()
	
