#!/usr/bin/python3
""" Creates and distributes an archive to web servers,
using created function deploy and pack"""

from fabric.api import *
from datetime import datetime
import os

env.hosts = ['35.153.143.199', '44.210.236.124']


def deploy():
    """Pack and deploy all files"""
    try:
        archive_path = do_pack()
    except Exception:
        return False

    return do_deploy(archive_path)
    
    
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


def do_deploy(archive_path):
    """Deploy archive file

    Args:
        archive_path - path of archive file
    """

    if os.path.exists(archive_path):
        try:
            """Split archive path"""
            archive = archive_path.split('/')[1]
            dirname = archive.split('.')[0]

            """Save folder paths in variables"""
            path = '/data/web_static/releases/{}'.format(dirname)
            tmp_location = '/tmp/{}'.format(archive)

            """Upload archive to the server"""
            put(archive_path, '/tmp/')

            """Run remote commands on the server"""
            run('mkdir -p {}'.format(path))
            run('tar -xzf {} -C {}'.format(tmp_location, path))
            run('rm {}'.format(tmp_location))
            run('mv {}/web_static/* {}'.format(path, path))
            run('rm -rf {}/web_static'.format(path))
            run('rm -rf /data/web_static/current')
            run('ln -sf {} /data/web_static/current'.format(path))
            run('sudo service nginx restart')

            return True
        except Exception:
            return False
    else:
        return False

