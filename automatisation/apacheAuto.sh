#!/bin/bash
#Executer en tant que root

apt install apache2 libapache2-mod-python python-psycopg2

cp -rv /root/ATS-Project/www /var/

cp -rv /root/ATS-Project/www/server-config/apache2 /etc/

cp -rv /root/ATS-Project/www/server-config/ssl /etc/

systemctl restart apache2
