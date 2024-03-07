#!/usr/bin/python3
"""this extracts to web server
"""
import os
from fabric.api import *

env.hosts = ['54.159.26.191', '54.157.182.105']


def do_deploy(archive_path):
    """files to deploy"""
    try:
        print("Starting do_deploy function...")
        if not (path.exists(archive_path)):
            return False

        put(archive_path, "/tmp/")

        # uncompress the archive
        parts = archive_path.split('_')
        time_stamp = parts[2].split(".")[0]
        run("sudo rm -rf /data/web_static/releases/\
web_static_{}".format(time_stamp))
        run("sudo mkdir -p /data/web_static/releases/\
web_static_{}".format(time_stamp))
        run("sudo tar -xzf /tmp/web_static_{}.tgz -C /data/\
web_static/releases/web_static_{}".format(time_stamp, time_stamp))

        # delete the archive from web_server
        run("sudo rm -rf /tmp/web_static_{}.tgz".format(time_stamp))

        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(time_stamp, time_stamp))

        # delete the file
        run("sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static".format(time_stamp))
        # delete the symbolic link
        run("sudo rm -rf /data/web_static/current")

        # create a new symblolic link
        run("sudo ln -sf /data/web_static/releases/\
web_static_{} /data/web_static/current".format(time_stamp))

        return True
    except Exception as e:
        return False
