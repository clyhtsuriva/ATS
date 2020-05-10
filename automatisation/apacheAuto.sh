#!/bin/bash
#Executer en tant que root

apt install apache2 libapache2-mod-python python-psycopg2

cp -r /root/ATS-Project/www /var/

cp -r /root/ATS-Project/www/server-config/apache2 /etc/

cp -r /root/ATS-Project/www/server-config/ssl /etc/

systemctl restart apache2
