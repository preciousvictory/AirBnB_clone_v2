#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
import datetime
import os

def do_pack():
    """function do_pack!"""
    a = datetime.datetime.now()

    path = f"versions/web_static_{a.year}{a.month}{a.day}{a.hour}{a.minute}{a.second}.tgz"
    local("makdir -p versions")
    local(f"tar -cvf {path} web_static")

    if os.path.exists(path):
        return path
    return None
