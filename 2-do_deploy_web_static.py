#!/usr/bin/python3
# Deploy archive file to the server

import os
from fabric.api import *

# versions/web_static_20170315003959.tgz

env.hosts = ['35.153.143.199', '44.210.236.124']


def do_deploy(archive_path):
    """Deploy archive file

    Args:
        archive_path - path of archive file
    """

    if os.path.exists(archive_path):
        try:
            arch = archive_path.split('/')[1]
            dirn = arch.split('.')[0]
            path = '/data/web_static/releases/'

            put('{} /tmp/'.format(arch))

            run('mkdir -p path{}'.format(dirn))
            run('tar -xzf {} -C path{}'.format(arch, dirn))

            run('rm -rf /tmp/{}'.format(arch))
            run('mv path{}/web_static/* path{}/'.format(dirn, dirn))
            run('rm -rf path{}/web_static'.format(dirn))
            run('rm -rf /data/web_static/current')

            run('ln -s -f /data/web_static/current path{}'.format(dirn))

            return True
        except Exception:
            return False
    else:
        return False
