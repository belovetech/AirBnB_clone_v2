#!/usr/bin/python3
""" Creates and distributes an archive to web servers,
using created function deploy and pack"""

from fabric.api import *
import os

do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

env.hosts = ['35.153.143.199', '44.210.236.124']


def deploy():
    """Pack and deploy all files"""
    try:
        archive_path = do_pack()
    except Exception:
        return False

    return do_deploy(archive_path)
