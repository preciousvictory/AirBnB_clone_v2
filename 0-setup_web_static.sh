#!/bin/bash
# a Bash script that sets up your web servers for the deployment of web_static.
DIR=/data/web_static/releases/test/
if ![ -d $DIR ]
then
	mkdir -p "/data/web_static/releases/test/"
fi

FILE=/data/web_static/releases/test/
if ![ -f $FILE ]
then
	touch "/data/web_static/releases/test/index.html"
	echo "Hello AirBnB Clone!"
fi

ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -fR ubuntu:ubuntu /data/

ser="\
server {
	location /data/web_static/current/ {
		alias https://victorycodes.tech/hbnb_static;
		autoindex off;
	}
}"

echo "$ser" >> /etc/nginx/sites-available/default
sudo service nginx restart
