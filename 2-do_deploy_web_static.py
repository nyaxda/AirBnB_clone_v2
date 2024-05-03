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
    result = put(archive_path, "/tmp/")
    if result.failed:
        return False
    archive_name = os.path.basename(archive_path)
    name, ext = os.path.splitext(archive_name)
    result = run("mkdir -p /data/web_static/releases/{}/".format(name))
    if result.failed:
        return False
    result = run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
        archive_name, name))
    if result.failed:
        return False
    result = run("rm /tmp/{}".format(archive_name))
    if result.failed:
        return False
    result = run("rm -rf /data/web_static/current")
    if result.failed:
        return False
    result = run("""ln -s /data/web_static/releases/{}
        /data/web_static/current""".format(name))
    if result.failed:
        return False
    return True

