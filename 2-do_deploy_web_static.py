#!/usr/bin/python3
"""this extracts to web server
"""
import os
from fabric.api import *

env.hosts = ['54.159.26.191', '54.157.182.105']


def do_deploy(archive_path):
    """this function distributes the file"""
    if os.path.exists(archive_path):
        try:
            filename = archive_path.split('/')[-1]
            direc = filename.split('.')[0]
            put(archive_path, '/tmp/')
            fname = f'/data/web_static/releases/{direc}'
            run(f"sudo mkdir -p /data/web_static/releases/{direc}")
            run(f'sudo tar -xzf /tmp/{filename} -C {fname}')
            run(f'sudo rm /tmp/{filename}')
            run(f'mv {fname}/web_static/* {fname}/')
            run(f'sudo rm -f /data/web_static/current')
            run(f'sudo ln -sf {fname}/ /data/web_static/current')
            return True
        except Exception as e:
            return False
    else:
        return False
