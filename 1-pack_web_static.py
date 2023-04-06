#!/usr/bin/python3
#!/usr/bin/env bash
"""
a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """function do_pack!"""

    path = f"versions/web_static_{}.tgz".format(
            datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))

    local("makdir -p versions")
    r = local(f"tar -cvzf {path} web_static")

    if r.failed:
        return path
    return None
