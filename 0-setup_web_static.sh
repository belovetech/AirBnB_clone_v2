#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# Install Nginx
apt-get install -y nginx


# Create web_static path
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared
touch /data/web_static/releases/test/index.html

# Print 'Hello Nginx'
echo "Hello Nginx!" >> /data/web_static/releases/test/index.html

# Create a symbolink link
ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu
chown -hR "ubuntu":"ubuntu" /data

# Update Nginx configuration
sed -i "38i\\\tlocation /hbnb_static/{\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart

