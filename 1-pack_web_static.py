#!/usr/bin/python3

# Fabric script that generates a .tgz archive
# from the contents of the web_static folder of your AirBnB Clone repo

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generate a .tgz archive from the contents of the web_static"""
    try:
        now = datetime.now()
        format_now = now.strftime('%Y%m%d%H%M%S')
        local('mkdir -p versions')

        archive_path = 'versions/web_static_{}.tgz'.format(format_now)
        local('tar -czvf {} web_static'.format(archive_path))
        return archive_path

    except Exception:
        return None
