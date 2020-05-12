#!/bin/bash
# coding: utf-8

#TO-DO:
#prend en compte l'interface internet par defaut sur la machine
#recupere l'adresse IP lie a cette interface
#installe tcpdump avant toute chose
#corrige le deplacement du cut dans certaines trames (comme ARP)
#Affiche quelque chose d'autre que "IP" en protocole (probleme pour la plupart des paquets
#enleve ce qu'il y a apres la virgule pour les secondes
#ajoute la date
#insert dans la bdd les differentes infos

#sudo tcpdump -i wlp2s0 -c1 -v -w temp.pcap
#b=$(sudo tcpdump -r temp.pcap > tempcat)
#cat tempcat 
#a=$(cat tempcat | cut -d" " -f13)

#echo "$a"

#if [ "$a" == "TCP" ] ; then
#	echo 'Youpi'
#elif [ "$a" == "UDP" ] ; then
#	echo 'Ah bah non ça marche pas'
#else 
#	echo 'KC'
#fi

while :
do

	sudo tcpdump -i wlp2s0 -c1 -nn tcp -w capturetcp.pcap
	sudo tcpdump -nn -r capturetcp.pcap > grostastcp
	echo -e "Voici un paquet TCP\n"
	cat grostastcp | cut -d" " -f1 >> /tmp/heuretcp.txt
	cat grostastcp | cut -d" " -f2 >> /tmp/protocoletcp.txt
	cat grostastcp | cut -d" " -f3 >> /tmp/sourcetcp.txt
	cat grostastcp | cut -d" " -f5 >> /tmp/destinationtcp.txt
	cat grostastcp | cut -d" " -f15 >> /tmp/tailletcp.txt
	tail -n1 /tmp/heuretcp.txt
	tail -n1 /tmp/protocoletcp.txt
	tcpvar=$(tail -n1 /tmp/sourcetcp.txt)
	echo "${tcpvar%.*}" >> /tmp/ipsrctcp.txt
	echo "${tcpvar##*.}" >> /tmp/portsrctcp.txt
	tail -n1 /tmp/ipsrctcp.txt
	tail -n1 /tmp/portsrctcp.txt	
	tcprav=$(tail -n1 /tmp/destinationtcp.txt)
	echo "${tcprav%.*}" >> /tmp/ipdsttcp.txt
	echo "${tcprav##*.}" | cut -d":" -f1 >> /tmp/portdsttcp.txt
	tail -n1 /tmp/ipdsttcp.txt
	tail -n1 /tmp/portdsttcp.txt
	tail -n1 /tmp/tailletcp.txt

# Attention ici c'est UDP

	sudo tcpdump -i wlp2s0 -c1 -nn udp -w captureudp.pcap
	sudo tcpdump -nn -r captureudp.pcap > grostasudp
	echo -e "Voici un paquet UDP\n" 
	cat grostasudp | cut -d" " -f1 >> /tmp/heureudp.txt
	cat grostasudp | cut -d" " -f2 >> /tmp/protocoleudp.txt
	cat grostasudp | cut -d" " -f3 >> /tmp/sourceudp.txt
	cat grostasudp | cut -d" " -f5 >> /tmp/destinationudp.txt
	cat grostasudp | cut -d" " -f8 >> /tmp/tailleudp.txt
	tail -n1 /tmp/heureudp.txt
	tail -n1 /tmp/protocoleudp.txt
	udpvar=$(tail -n1 /tmp/sourceudp.txt)
	echo "${udpvar%.*}" >> /tmp/ipsrcudp.txt
	echo "${udpvar##*.}" >> /tmp/portsrcudp.txt
	tail -n1 /tmp/ipsrcudp.txt
	tail -n1 /tmp/portsrcudp.txt	
	udprav=$(tail -n1 /tmp/destinationudp.txt)
	echo "${udprav%.*}" >> /tmp/ipdstudp.txt
	echo "${udprav##*.}" | cut -d":" -f1 >> /tmp/portdstudp.txt
	tail -n1 /tmp/ipdstudp.txt
	tail -n1 /tmp/portdstudp.txt
	tail -n1 /tmp/tailleudp.txt
done
