#!/usr/bin/env bash

#update and install nginx if not installed
apt-get update && apt-get install -y nginx

#enable traffic ib port 80

ufw allow'HTTP'

#restart nginx
service nginx restart
