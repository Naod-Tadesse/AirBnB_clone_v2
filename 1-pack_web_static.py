#!/usr/bin/python3
"""create archive from webstatic"""
from datetime import datetime
from fabric.api import local
from time import strftime


def do_pack():
    """create the zip file"""
    fname = f'web_static_{datetime.now().strftime("%Y%m%d%H%M%S")}'
    local("mkdir -p versions/")
    save = local(f"tar -cvzf versions/{fname}.tgz web_static")
    if not save.failed:
        return f"versions/{fname}"
    else:
        return None
