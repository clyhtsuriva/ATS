#!/bin/bash
#cloner dans le repertoire personnel du root
#exucuter en tant que root

cp /root/ATS-Project/www/html/init-bd.sql /tmp/table.sql #Car problème de droit root

apt install postgresql

useradd atsuser

echo atsuser:123456 | chpasswd


echo "CREATE USER atsuser WITH PASSWORD '123456'; CREATE DATABASE atsdb; GRANT ALL PRIVILEGES ON DATABASE atsdb to atsuser;" > /tmp/conf

service postgresql start #dernier ajout : Lancement du serveur

su - postgres -c "psql -f /tmp/conf" #creation de l'util atsuser et la bdd atsdb sur le serv psql


pushd /tmp ; su atsuser -c "psql -d atsdb -U atsuser -f /tmp/table.sql" ; popd #mis en place de la table paquet dans la bdd

