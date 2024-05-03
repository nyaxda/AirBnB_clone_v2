#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

if ! command -v nginx &> /dev/null
then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "<!DOCTYPE html>
<html>
<head>
  <title>Test Page</title>
</head>
<body>
  <h1>This is a test page</h1>
  <p>Hello, world!</p>
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html >/dev/null
target="/data/web_static/releases/test"
link="/data/web_static/current"
if [ -L "$link" ]; then
    sudo rm "$link"
fi
sudo ln -s "$target" "$link"

sudo chown -R ubuntu:ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served by $hostname;
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location = /404.html{
        internal;
    }
}" > /etc/nginx/sites_available/default

service nginx restart
