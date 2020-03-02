#!/bin/bash

while :
do

	sudo tcpdump -i eth1 -nn -c1 -A src 192.168.52.19 -w capture.pcap 
	sudo tcpdump -r capture.pcap > grostas 
	cat grostas | cut -d" " -f1 >> heure.txt
	cat grostas | cut -d" " -f2 >> protocole.txt
	cat grostas | cut -d" " -f3 >> source.txt
	cat grostas | cut -d" " -f5 >> destination.txt	
	tail -n1 heure.txt
	tail -n1 protocole.txt
	tail -n1 source.txt
	tail -n1 destination.txt
done



