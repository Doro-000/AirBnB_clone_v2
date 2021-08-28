#!/usr/bin/python3
"""deletes out-of-date archives"""
from fabric.api import *
from os import walk

env.hosts = ['34.138.61.3', '34.75.118.132']
env.user = "ubuntu"


def do_clean(number=0):
    """deletes out-of-date archives"""
    number = int(number)
    [*unparsed_result] = walk("./versions")
    with cd("/data/web_static/releases"):
        unparsed_result_2 = run("ls -t .")
    if (unparsed_result):
        result = unparsed_result[0][2][::-1]
        if (len(result) > 1):
            if (number == 0 or number == 1):
                num = 1
            else:
                num = number
            try:
                for tar in result[num:]:
                    with lcd("./versions"):
                        local("rm -f {}".format(tar))
            except:
                pass
    if (unparsed_result_2):
        result_2 = unparsed_result_2.split()
        if (len(result_2) > 1):
            if (number == 0 or number == 1):
                num = 1
            else:
                num = number
            for file in result_2[num:]:
                run("rm -rf /data/web_static/releases/{}".format(file))
