#!/usr/bin/python3
"""create archive from webstatic"""
from datetime import datetime
from fabric.api import local

def do_pack():
    fname = f'web_static_{datetime.now().strftime("%Y%m%d%H%M%S")}'
    local("mkdir -p versions/")
    save = local(f"tar -cvzf versions/{fname} web_static")
    if not result.failed:
        return f"versions/fname"
    else:
        return None
