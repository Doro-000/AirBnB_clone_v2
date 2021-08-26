#!/usr/bin/python3
"""deletes out-of-date archives"""
from fabric.api import *

env.hosts = ['34.138.61.3', '34.75.118.132']
env.user = "ubuntu"


def do_clean(number=0):
    """deletes out-of-date archives"""
    with lcd("./versions"):
        unparsed_result = local("ls -t .")
    if (unparsed_result):
        result = unparsed_result.split()
        if (len(result) > 1):
            if (number == 0 or number == 1):
                num = 1
            try:
                for tar in result[num:]:
                    local("rm ./versions/{}".format(tar))
                    name = tar.split(".")[0]
                    run("rm -rf /data/web_static/releases/{}".format(name))
            except:
                pass
    else:
        pass
