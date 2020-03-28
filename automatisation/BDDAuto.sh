#!/bin/bash

cp /root/ATS-Project/web/website/init-bd.sql /tmp/table.sql #Car problème de droit root

apt install postgresql

useradd atsuser

echo atsuser:123456 | chpasswd


echo "CREATE USER atsuser WITH PASSWORD '123456'; CREATE DATABASE atsdb; GRANT ALL PRIVILEGES ON DATABASE atsdb to atsuser;" > /tmp/conf


su - postgres -c "psql -f /tmp/conf"

su - atsuser -c "psql -d atsdb -U atsuser -f /tmp/table.sql"
