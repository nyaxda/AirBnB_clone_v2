#!/usr/bin/python3
# Fabfile
from fabric.api import env, run, put
import os.path

env.hosts = ['100.25.170.102',
             '100.24.236.169'
             ]


def do_deploy(archive_path):
    """Deploy an archive to the web servers."""
    if os.path.isfile(archive_path) is False:
        return False
    archive_name = os.path.basename(archive_path)
    name, ext = os.path.splitext(archive_name)
    if put(archive_path, "/tmp/").failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".format(
            name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            archive_name, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(archive_name)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".format(
            name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("""ln -s /data/web_static/releases/{}/
           /data/web_static/current""".format(name)).failed is True:
        return False
    return True
