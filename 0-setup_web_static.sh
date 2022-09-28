#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared
touch /data/web_static/releases/test/index.html

ln -s -f /data/web_static/releases/test/ /data/web_static/current
chown -R $USER:$USER /data

printf %s "{
		
	location /hbnb_static {
		alias /
	}

}" >> /ete/nginx/sites-available/default

