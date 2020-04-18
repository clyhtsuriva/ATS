#!/bin/bash

#TO-DO:
#prend en compte l'interface internet par defaut sur la machine
#recupere l'adresse IP lie a cette interface
#installe tcpdump avant toute chose
#corrige le deplacement du cut dans certaines trames (comme ARP)
#Affiche quelque chose d'autre que "IP" en protocole (probleme pour la plupart des paquets
#enleve ce qu'il y a apres la virgule pour les secondes
#ajoute la date
#insert dans la bdd les differentes infos

while :
do

	sudo tcpdump -i eth1 -nn -c1 -A src $1 -w capture.pcap
	sudo tcpdump -r capture.pcap > grostas
	cat grostas | cut -d" " -f1 >> /tmp/heure.txt
	cat grostas | cut -d" " -f2 >> /tmp/protocole.txt
	cat grostas | cut -d" " -f3 >> /tmp/source.txt
	cat grostas | cut -d" " -f5 >> /tmp/destination.txt
	tail -n1 /tmp/heure.txt
	tail -n1 /tmp/protocole.txt
	tail -n1 /tmp/source.txt
	tail -n1 /tmp/destination.txt
done



