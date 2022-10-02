#!/usr/bin/python3
# Deploy archive file to the server

import os
from fabric.api import *


env.hosts = ['35.153.143.199', '44.210.236.124']


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
            path = '/data/web_static/releases/'.format(dirname)
            tmp_location = '/tmp/{}'.format(archive)
            
            """Upload archive to the server"""
            put(archive_path, '/tmp/')

            """Run remote commands on the server"""
            run('mkdir -p path{}'.format(path))
            run('tar -xvzf {} -C {}'.format(tmp_location, path))
            run('rm -rf {}'.format(tmp_location))
            run('mv {}/web_static/* {}/'.format(path, path))
            run('rm -rf {}/web_static'.format(path))
            run('rm -rf /data/web_static/current')
            run('ln -sf {} /data/web_static/current'.format(path))
            run('sudo service nginx restart')

            return True
        except Exception:
            return False
    else:
        return False
