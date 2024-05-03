#!/usr/bin/python3
# Fabfile
from fabric.api import env, run, put
from fabric.exceptions import CommandError
import os.path

env.hosts = ['100.25.170.102',
             '100.24.236.169'
             ]


def do_deploy(archive_path):
    """Deploy an archive to the web servers."""
    if os.path.isdir(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        archive_name = os.path.basename(archive_path)
        name, ext = os.path.splitext(archive_name)
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            archive_name, name))
        run("rm /tmp/{}".format(archive_name))
        run("rm -rf /data/web_static/current")
        run("""ln -s /data/web_static/releases/{}
            /data/web_static/current""".format(name))
    except CommandError:
        return False
    return True
