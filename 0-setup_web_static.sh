#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static.
# Install Nginx if it not already installed
if ! [ -d $n ]
then
        sudo apt-get -y update
        sudo apt-get -y install nginx
        echo 'Hello World!' > /var/www/html/index.html
        service nginx start
fi

# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
DIR=/data/web_static/releases/test/
if ! [ -d $DIR ]
then
        mkdir -p /data/web_static/releases/test/
fi

# Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
FILE=/data/web_static/releases/test/
if ! [ -f $FILE ]
then
        touch /data/web_static/releases/test/index.html
        echo "<html>
        <head>
        </head>
        <body>
                AirBnB Clone!
        </body>
        </html>" > /data/web_static/releases/test/index.html
fi

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
touch /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -fR ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static). 
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default

sudo service nginx restart
