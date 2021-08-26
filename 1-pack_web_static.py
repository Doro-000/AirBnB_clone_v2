#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """creates a tarfile"""
    local("mkdir -p versions")
    now = datetime.now()
    tar_file = "web_static_{}{}{}{}{}{}.tgz".format(now.year, now.month,
    now.day, now.hour, now.minute, now.second)
    local("tar -cvzf  versions/{} web_static".format(tar_file))
