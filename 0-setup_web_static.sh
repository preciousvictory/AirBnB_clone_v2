#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static.
# Install Nginx if it not already installed
sudo apt-get -y update
sudo apt-get -y install nginx
echo 'Hello World!' > /var/www/html/index.html
mkdir -p /data/web_static/releases/test/

touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

ln -sf '/data/web_static/releases/test/' '/data/web_static/current'

sudo chown -fR ubuntu:ubuntu /data 
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart
