#!/usr/bin/python3
# Fabfile
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy


env.hosts = ["100.25.170.102", "100.24.236.169"]

def deploy():
    """Creates and distributes an archive to a web server."""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
